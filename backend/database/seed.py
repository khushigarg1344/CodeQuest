
import json

from database.database import SessionLocal
from database.models import Problem, Badge
from database.dsa_question_bank import DSA_PROBLEMS


# ==========================================
# INITIAL PROBLEMS
# ==========================================

PROBLEMS = [

    {
        "title": "Find Maximum",
        "description": "Given an integer array, find and print the maximum element.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5\n1 8 3 2 6",
        "sample_output": "8",
        "test_cases_json": json.dumps([
            {"input": "5\n1 8 3 2 6", "output": "8"},
            {"input": "4\n-5 -2 -9 -1", "output": "-1"},
            {"input": "3\n7 7 2", "output": "7"}
        ])
    },

    {
        "title": "Reverse an Array",
        "description": "Given an integer array, print the elements in reverse order.",
        "difficulty": "Easy",
        "topic": "Arrays",
        "xp_reward": 50,
        "sample_input": "5\n1 2 3 4 5",
        "sample_output": "5 4 3 2 1",
        "test_cases_json": json.dumps([
            {"input": "5\n1 2 3 4 5", "output": "5 4 3 2 1"}
        ])
    },

    {
        "title": "Two Sum",
        "description": "Given an array and a target, find two numbers whose sum equals the target.",
        "difficulty": "Medium",
        "topic": "Arrays",
        "xp_reward": 100,
        "sample_input": "4 9\n2 7 11 15",
        "sample_output": "0 1",
        "test_cases_json": json.dumps([
            {"input": "4 9\n2 7 11 15", "output": "0 1"}
        ])
    }

]


# ==========================================
# INITIAL BADGES
# ==========================================

BADGES = [

    (
        "First Quest",
        "Solve your first coding quest.",
        "🎯"
    ),

    (
        "XP Hunter",
        "Earn at least 100 XP.",
        "⭐"
    )

]


# ==========================================
# SEED DATABASE
# ==========================================

def seed_database():

    db = SessionLocal()

    try:

        # --------------------------------------
        # GET EXISTING PROBLEM TITLES
        # --------------------------------------

        existing_titles = {
            title for (title,) in db.query(Problem.title).all()
        }

        # --------------------------------------
        # INSERT INITIAL PROBLEMS
        # --------------------------------------

        for problem in PROBLEMS:

            if problem["title"] not in existing_titles:

                db.add(Problem(**problem))
                existing_titles.add(problem["title"])

        # --------------------------------------
        # INSERT DSA QUESTION BANK
        # --------------------------------------

        for problem in DSA_PROBLEMS:

            if problem["title"] not in existing_titles:

                db.add(Problem(**problem))
                existing_titles.add(problem["title"])

        # --------------------------------------
        # GET EXISTING BADGES
        # --------------------------------------

        existing_badges = {
            name for (name,) in db.query(Badge.name).all()
        }

        # --------------------------------------
        # INSERT MISSING BADGES
        # --------------------------------------

        for name, description, icon in BADGES:

            if name not in existing_badges:

                db.add(
                    Badge(
                        name=name,
                        description=description,
                        icon=icon
                    )
                )

                existing_badges.add(name)

        # --------------------------------------
        # SAVE CHANGES
        # --------------------------------------

        db.commit()

        print("CodeQuest database seeding completed!")
        print(f"Total problems in database: {db.query(Problem).count()}")

    except Exception as exc:

        db.rollback()
        print(f"Database seeding failed: {exc}")
        raise

    finally:

        db.close()
