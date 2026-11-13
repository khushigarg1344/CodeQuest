
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime,
    Date,
    Boolean,
    UniqueConstraint
)

from sqlalchemy.orm import relationship

from .database import Base


# ==========================================
# USER
# ==========================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, index=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    xp = Column(Integer, default=0)

    level = Column(Integer, default=1)

    streak = Column(Integer, default=0)

    submissions = relationship("Submission", back_populates="user")

    badges = relationship("UserBadge", back_populates="user")

    lesson_progress = relationship(
        "UserLessonProgress",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    daily_challenge_completions = relationship(
        "DailyChallengeCompletion",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# ==========================================
# PROBLEM
# ==========================================

class Problem(Base):

    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    description = Column(Text, nullable=False)

    difficulty = Column(String(30), default="Easy")

    topic = Column(String(100), nullable=False)

    xp_reward = Column(Integer, default=50)

    sample_input = Column(Text, default="")

    sample_output = Column(Text, default="")

    test_cases_json = Column(Text, default="[]")

    submissions = relationship("Submission", back_populates="problem")


# ==========================================
# SUBMISSION
# ==========================================

class Submission(Base):

    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(Text, nullable=False)

    language = Column(String(30), default="java")

    status = Column(String(50), nullable=False)

    output = Column(Text, default="")

    error = Column(Text, default="")

    passed = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))

    problem_id = Column(Integer, ForeignKey("problems.id"))

    user = relationship("User", back_populates="submissions")

    problem = relationship("Problem", back_populates="submissions")


# ==========================================
# BADGE
# ==========================================

class Badge(Base):

    __tablename__ = "badges"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), unique=True)

    description = Column(Text)

    icon = Column(String(20), default="🏆")

    users = relationship("UserBadge", back_populates="badge")


# ==========================================
# USER BADGE
# ==========================================

class UserBadge(Base):

    __tablename__ = "user_badges"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    badge_id = Column(Integer, ForeignKey("badges.id"))

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="badges")

    badge = relationship("Badge", back_populates="users")


# ==========================================
# USER LESSON PROGRESS
# ==========================================

class UserLessonProgress(Base):

    __tablename__ = "user_lesson_progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    lesson_id = Column(
        String(150),
        nullable=False,
        index=True
    )

    completed = Column(Boolean, default=False, nullable=False)

    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="lesson_progress")

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "lesson_id",
            name="unique_user_lesson"
        ),
    )


# ==========================================
# DAILY CHALLENGE COMPLETION
# ==========================================

class DailyChallengeCompletion(Base):

    __tablename__ = "daily_challenge_completions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    problem_id = Column(
        Integer,
        ForeignKey("problems.id"),
        nullable=False
    )

    challenge_date = Column(
        Date,
        nullable=False,
        index=True
    )

    completed_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="daily_challenge_completions"
    )

    problem = relationship("Problem")

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "challenge_date",
            name="unique_user_daily_challenge"
        ),
    )
