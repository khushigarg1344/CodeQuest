
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User, Badge, UserBadge
from routes.users import get_current_user


router = APIRouter(
    prefix="/api/badges",
    tags=["Badges"]
)


@router.get("/")
def get_user_badges(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_badges = (
        db.query(UserBadge, Badge)
        .join(Badge, UserBadge.badge_id == Badge.id)
        .filter(UserBadge.user_id == user.id)
        .all()
    )

    return {
        "total_badges": len(user_badges),
        "badges": [
            {
                "id": badge.id,
                "name": badge.name,
                "description": badge.description,
                "icon": badge.icon
            }
            for user_badge, badge in user_badges
        ]
    }
