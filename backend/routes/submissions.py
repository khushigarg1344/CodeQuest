
import json
import requests

from datetime import datetime,timedelta
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import (
    Submission,
    Problem,
    User,
    DailyChallengeCompletion
)

from routes.users import (
    award_streak_badges,
    get_current_user,
    get_solved_count,
    award_badges
)

from services.judge0 import execute_code


router = APIRouter(
    prefix="/api/submissions",
    tags=["Submissions"]
)


# Request model for code submission
class CodeSubmissionRequest(BaseModel):

    code: str = Field(min_length=1, max_length=20000)

    language: str


# Existing submission history model
class SubmissionHistoryItem(BaseModel):

    problem_id: int | None

    code: str

    language: str

    status: str

    output: str | None = None

    error: str | None = None

    passed: bool


# ------------------------------------------------
# HELPER: GET TODAY'S DAILY CHALLENGE
# ------------------------------------------------

def get_todays_daily_challenge(db: Session):

    today = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).date()

    problems = (
        db.query(Problem)
        .filter(
            Problem.topic.isnot(None),
            Problem.topic != ""
        )
        .order_by(Problem.id.asc())
        .all()
    )

    if not problems:
        return None, today

    day_number = today.toordinal()

    question_index = day_number % len(problems)

    return problems[question_index], today


# ------------------------------------------------
# 1. GET SUBMISSION HISTORY
# ------------------------------------------------

@router.get("/me")
def my_submissions(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    items = (
        db.query(Submission)
        .filter(Submission.user_id == user.id)
        .order_by(Submission.created_at.desc())
        .limit(100)
        .all()
    )

    return [
        {
            "id": item.id,
            "problem_id": item.problem_id,
            "code": item.code,
            "language": item.language,
            "status": item.status,
            "output": item.output,
            "error": item.error,
            "passed": item.passed,
            "created_at": (
                item.created_at.isoformat()
                if item.created_at else None
            )
        }
        for item in items
    ]


# ------------------------------------------------
# 2. RUN CODE USING JUDGE0
# ------------------------------------------------

@router.post("/{problem_id}/run")
def run_submission(
    problem_id: int,
    payload: CodeSubmissionRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # Step 1: Find the requested problem

    problem = (
        db.query(Problem)
        .filter(Problem.id == problem_id)
        .first()
    )

    if not problem:
        raise HTTPException(
            status_code=404,
            detail="Problem not found."
        )

    # Step 2: Validate programming language

    language = payload.language.lower().strip()

    if language not in ["python", "java", "cpp"]:

        raise HTTPException(
            status_code=400,
            detail="Supported languages: Python, Java and C++."
        )

    # Step 3: Read test cases from database

    try:

        test_cases = json.loads(
            problem.test_cases_json or "[]"
        )

    except json.JSONDecodeError:

        raise HTTPException(
            status_code=500,
            detail="Invalid test cases stored for this problem."
        )

    if not test_cases:

        raise HTTPException(
            status_code=500,
            detail="No test cases available for this problem."
        )

    passed_count = 0

    final_status = "Accepted"

    final_output = ""

    final_error = ""

    # Step 4: Execute code against each test case

    try:

        for test in test_cases:

            result = execute_code(
                source_code=payload.code,
                language=language,
                stdin=test["input"]
            )

            actual_output = (
                result.get("output") or ""
            ).strip()

            expected_output = str(
                test.get("output", "")
            ).strip()

            status_id = result.get("status_id")

            if status_id != 3:

                final_status = (
                    result.get("status")
                    or "Execution Error"
                )

                final_error = (
                    result.get("error") or ""
                )

                final_output = actual_output

                break

            actual_normalized = " ".join(
                actual_output.split()
            )

            expected_normalized = " ".join(
                expected_output.split()
            )

            if actual_normalized != expected_normalized:

                final_status = "Wrong Answer"

                final_output = actual_output

                break

            passed_count += 1

            final_output = actual_output

    except requests.RequestException:

        raise HTTPException(
            status_code=502,
            detail="Judge0 connection failed. Please try again."
        )

    except (TimeoutError, RuntimeError, ValueError) as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc)
        )

    # Step 5: Check previous successful submission

    already_solved = (
        db.query(Submission)
        .filter(
            Submission.user_id == user.id,
            Submission.problem_id == problem_id,
            Submission.passed.is_(True)
        )
        .first()
        is not None
    )

    all_passed = passed_count == len(test_cases)

    if all_passed:

        final_status = "Accepted"

    # Step 6: Save submission

    submission = Submission(
        code=payload.code,
        language=language,
        status=final_status,
        output=final_output,
        error=final_error,
        passed=all_passed,
        user_id=user.id,
        problem_id=problem.id
    )

    db.add(submission)

    # Step 7: Award XP only once per problem

    awarded_xp = 0

    if all_passed and not already_solved:

        awarded_xp = problem.xp_reward or 25

        user.xp = (user.xp or 0) + awarded_xp

        user.level = user.xp // 100 + 1

    # Step 8: Record Daily Challenge completion

    daily_challenge_completed = False

    already_completed_today = False

    if all_passed:

       daily_problem, today = get_todays_daily_challenge(db)

       if daily_problem and daily_problem.id == problem_id:

        existing_completion = (
            db.query(DailyChallengeCompletion)
            .filter(
                DailyChallengeCompletion.user_id == user.id,
                DailyChallengeCompletion.challenge_date == today
            )
            .first()
        )

        if existing_completion:

            already_completed_today = True

        else:

            completion = DailyChallengeCompletion(
                user_id=user.id,
                problem_id=problem_id,
                challenge_date=today
            )

            db.add(completion)
            db.flush()

            daily_challenge_completed = True

        # Calculate the current consecutive-day streak.
        completed_dates = {
            row[0]
            for row in (
                db.query(DailyChallengeCompletion.challenge_date)
                .filter(
                    DailyChallengeCompletion.user_id == user.id,
                    DailyChallengeCompletion.challenge_date <= today
                )
                .all()
            )
        }

        current_streak = 0
        check_date = today

        while check_date in completed_dates:
            current_streak += 1
            check_date -= timedelta(days=1)

    # Award streak achievements.
        award_streak_badges(
            db=db,
            user=user,
            current_streak=current_streak
        )

    # Step 9: Award badges for solved problems

    if all_passed:

        db.flush()

        solved_count = get_solved_count(
            db,
            user.id
        )

        award_badges(
            db,
            user,
            solved_count
        )

    # Step 10: Save all changes

    try:

        db.commit()

        db.refresh(user)

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Could not save submission. Please try again."
        )

    # Step 11: Return response

    return {
        "message": (
            "All test cases passed!"
            if all_passed
            else "Some test cases failed."
        ),

        "status": final_status,

        "passed": all_passed,

        "passed_test_cases": passed_count,

        "total_test_cases": len(test_cases),

        "awarded_xp": awarded_xp,

        "already_solved": already_solved,

        "daily_challenge_completed": daily_challenge_completed,

        "already_completed_today": already_completed_today,

        "output": final_output,

        "error": final_error,

        "xp": user.xp or 0,

        "level": user.level or 1
    }
