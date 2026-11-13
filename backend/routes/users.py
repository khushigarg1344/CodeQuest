
from datetime import date, timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User, Submission, Problem, Badge, UserBadge
from utils.auth import decode_access_token


router = APIRouter(
    prefix="/api/users",
    tags=["Users and Progress"]
)

# Swagger JWT authentication
bearer_scheme = HTTPBearer()


# -----------------------------------------
# 1. GET CURRENT LOGGED-IN USER
# -----------------------------------------

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
) -> User:

    token = credentials.credentials

    user_id = decode_access_token(token)

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Your session is invalid or expired. Please log in again."
        )

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User account was not found."
        )

    return user


# -----------------------------------------
# 2. COUNT SOLVED PROBLEMS
# -----------------------------------------

def get_solved_count(db: Session, user_id: int) -> int:

    return (
        db.query(Submission.problem_id)
        .filter(
            Submission.user_id == user_id,
            Submission.passed.is_(True),
            Submission.problem_id.isnot(None)
        )
        .distinct()
        .count()
    )


# -----------------------------------------
# 3. AWARD BADGES
# -----------------------------------------

def award_badges(
    db: Session,
    user: User,
    solved_count: int
) -> None:

    milestones = [
    (1, "First Quest", "Solved your first coding problem.", "🎯"),

    (5, "Problem Solver", "Solved five different problems.", "⚡"),

    (10, "Code Explorer", "Solved ten different problems.", "🧭"),

    (20, "Rising Coder", "Solved twenty different problems.", "🚀"),

    (50, "DSA Master", "Solved fifty different problems.", "🏆"),

    (100, "CodeQuest Champion", "Solved one hundred different problems.", "👑")
]
    for threshold, name, description, icon in milestones:

        if solved_count < threshold:
            continue

        badge = (
            db.query(Badge)
            .filter(Badge.name == name)
            .first()
        )

        if not badge:
            badge = Badge(
                name=name,
                description=description,
                icon=icon
            )

            db.add(badge)
            db.flush()

        owned = (
            db.query(UserBadge)
            .filter(
                UserBadge.user_id == user.id,
                UserBadge.badge_id == badge.id
            )
            .first()
        )

        if not owned:
            db.add(
                UserBadge(
                    user_id=user.id,
                    badge_id=badge.id
                )
            )


def award_streak_badges(
    db: Session,
    user: User,
    current_streak: int
) -> None:

    milestones = [
        (3, "Consistency Starter", "Completed daily challenges for 3 consecutive days.", "🔥"),
        (7, "Weekly Warrior", "Completed daily challenges for 7 consecutive days.", "🌟"),
        (30, "Streak Legend", "Completed daily challenges for 30 consecutive days.", "💎")
    ]

    for threshold, name, description, icon in milestones:

        if current_streak < threshold:
            continue

        badge = (
            db.query(Badge)
            .filter(Badge.name == name)
            .first()
        )

        if not badge:
            badge = Badge(
                name=name,
                description=description,
                icon=icon
            )

            db.add(badge)
            db.flush()

        owned = (
            db.query(UserBadge)
            .filter(
                UserBadge.user_id == user.id,
                UserBadge.badge_id == badge.id
            )
            .first()
        )

        if not owned:
            db.add(
                UserBadge(
                    user_id=user.id,
                    badge_id=badge.id
                )
            )


# -----------------------------------------
# 4. USER PROFILE
# -----------------------------------------

@router.get("/me")
def my_profile(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    solved = get_solved_count(db, user.id)

    badge_count = (
        db.query(UserBadge)
        .filter(UserBadge.user_id == user.id)
        .count()
    )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "xp": user.xp or 0,
        "level": (user.xp or 0) // 100 + 1,
        "streak": user.streak or 0,
        "solved": solved,
        "badges": badge_count
    }


# -----------------------------------------
# 5. PRACTICE ENDPOINT
# -----------------------------------------

@router.post("/me/practice/{problem_id}")
def mark_practiced(
    problem_id: int,
    user: User = Depends(get_current_user),
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
            detail="Problem not found."
        )

    already_practiced = (
        db.query(Submission)
        .filter(
            Submission.user_id == user.id,
            Submission.problem_id == problem_id,
            Submission.passed.is_(True)
        )
        .first()
    )

    if already_practiced:
        return {
            "message": "You have already earned XP for this problem.",
            "awarded_xp": 0,
            "already_completed": True,
            "profile": _profile(db, user)
        }

    db.add(
        Submission(
            code="PRACTICE_RECORDED",
            language="not-run",
            status="practiced",
            output="Marked as practiced in the learning dashboard.",
            error="",
            passed=True,
            user_id=user.id,
            problem_id=problem.id
        )
    )

    xp_reward = problem.xp_reward or 25

    user.xp = (user.xp or 0) + xp_reward
    user.level = user.xp // 100 + 1

    today = date.today()

    last_practice = (
        db.query(Submission)
        .filter(
            Submission.user_id == user.id,
            Submission.passed.is_(True)
        )
        .order_by(Submission.created_at.desc())
        .offset(1)
        .first()
    )

    if last_practice and last_practice.created_at:

        last_day = last_practice.created_at.date()

        if last_day == today - timedelta(days=1):
            user.streak = (user.streak or 0) + 1

        elif last_day < today - timedelta(days=1):
            user.streak = 1

        elif last_day == today:
            user.streak = max(user.streak or 0, 1)

    else:
        user.streak = 1

    solved = get_solved_count(db, user.id)

    award_badges(db, user, solved)

    db.commit()
    db.refresh(user)

    return {
        "message": f"Practice saved. You earned {xp_reward} XP.",
        "awarded_xp": xp_reward,
        "already_completed": False,
        "profile": _profile(db, user)
    }


# -----------------------------------------
# 6. PROFILE HELPER
# -----------------------------------------

def _profile(db: Session, user: User):

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "xp": user.xp or 0,
        "level": (user.xp or 0) // 100 + 1,
        "streak": user.streak or 0,
        "solved": get_solved_count(db, user.id),
        "badges": (
            db.query(UserBadge)
            .filter(UserBadge.user_id == user.id)
            .count()
        )
    }


# -----------------------------------------
# 7. LEADERBOARD
# -----------------------------------------

@router.get("/leaderboard")
def leaderboard(db: Session = Depends(get_db)):

    users = (
        db.query(User)
        .order_by(User.xp.desc(), User.id.asc())
        .limit(10)
        .all()
    )

    return [
        {
            "rank": index + 1,
            "name": user.name,
            "xp": user.xp or 0,
            "level": (user.xp or 0) // 100 + 1
        }
        for index, user in enumerate(users)
    ]
