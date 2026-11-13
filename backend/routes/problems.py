
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import (
    Problem,
    User,
    DailyChallengeCompletion
)

from routes.users import get_current_user


router = APIRouter(
    prefix="/api/problems",
    tags=["Problems"]
)


# ==========================================
# GET ALL DSA PROBLEMS
# ==========================================

@router.get("/")
def get_problems(db: Session = Depends(get_db)):

    problems = (
        db.query(Problem)
        .order_by(Problem.id.asc())
        .all()
    )

    return [
        {
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "difficulty": item.difficulty,
            "topic": item.topic,
            "xp_reward": item.xp_reward,
            "sample_input": item.sample_input,
            "sample_output": item.sample_output
        }
        for item in problems
    ]


# ==========================================
# GET DAILY CHALLENGE
# ==========================================

@router.get("/daily")
def get_daily_challenge(db: Session = Depends(get_db)):

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
        raise HTTPException(
            status_code=404,
            detail="No DSA questions available"
        )

    day_number = today.toordinal()

    question_index = day_number % len(problems)

    item = problems[question_index]

    return {
        "challenge_date": today.isoformat(),
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "difficulty": item.difficulty,
        "topic": item.topic,
        "xp_reward": item.xp_reward,
        "sample_input": item.sample_input,
        "sample_output": item.sample_output
    }


# ==========================================
# GET DAILY CHALLENGE PROGRESS
# ==========================================

@router.get("/daily/progress")
def get_daily_challenge_progress(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    today = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).date()

    # Get all completed daily challenges
    records = (
        db.query(DailyChallengeCompletion)
        .filter(
            DailyChallengeCompletion.user_id == user.id,
            DailyChallengeCompletion.challenge_date <= today
        )
        .order_by(
            DailyChallengeCompletion.challenge_date.asc()
        )
        .all()
    )

    # Extract unique completed dates
    completed_dates = sorted({
        record.challenge_date
        for record in records
    })

    completed_date_set = set(completed_dates)

    completed_today = today in completed_date_set

    # --------------------------------------
    # CURRENT STREAK
    # --------------------------------------

    current_streak = 0

    streak_date = (
        today
        if completed_today
        else today - timedelta(days=1)
    )

    while streak_date in completed_date_set:

        current_streak += 1

        streak_date -= timedelta(days=1)

    # --------------------------------------
    # LONGEST STREAK
    # --------------------------------------

    longest_streak = 0
    temporary_streak = 0
    previous_date = None

    for completed_date in completed_dates:

        if (
            previous_date is not None
            and completed_date == previous_date + timedelta(days=1)
        ):
            temporary_streak += 1

        else:
            temporary_streak = 1

        longest_streak = max(
            longest_streak,
            temporary_streak
        )

        previous_date = completed_date

    # --------------------------------------
    # RESPONSE
    # --------------------------------------

    return {
        "today": today.isoformat(),
        "completed_today": completed_today,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "total_completed_days": len(completed_dates),
        "completed_dates": [
            date.isoformat()
            for date in completed_dates
        ]
    }


# ==========================================
# GET SINGLE PROBLEM BY ID
# ==========================================

@router.get("/{problem_id}")
def get_problem(
    problem_id: int,
    db: Session = Depends(get_db)
):

    problem = (
        db.query(Problem)
        .filter(Problem.id == problem_id)
        .first()
    )

    if not problem:
        raise HTTPException(
            status_code=404,
            detail="Problem not found"
        )

    return {
        "id": problem.id,
        "title": problem.title,
        "description": problem.description,
        "difficulty": problem.difficulty,
        "topic": problem.topic,
        "xp_reward": problem.xp_reward,
        "sample_input": problem.sample_input,
        "sample_output": problem.sample_output
    }
