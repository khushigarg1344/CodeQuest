
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import User, UserLessonProgress
from routes.users import get_current_user

from learning_content import PYTHON_FOUNDATIONS, DSA_TRACK


router = APIRouter(
    prefix="/api/learning",
    tags=["Learning Paths"]
)

XP_PER_LESSON = 10


# ==========================================
# LEARNING PATH CONFIGURATION
# ==========================================


def build_modules(lesson_catalog, module_definitions):
    """
    Organize lessons from the content catalog into modules.
    Ensure every lesson has its correct ID.
    """

    modules = []

    for module_data in module_definitions:

        lessons = []

        for lesson_id in module_data["lesson_ids"]:

            lesson = lesson_catalog.get(lesson_id)

            if lesson:
                # Copy lesson to avoid modifying original content
                lesson_data = dict(lesson)

                # Restore the correct catalog ID if missing
                lesson_data.setdefault("id", lesson_id)

                # Provide a default duration if missing
                lesson_data.setdefault("duration", "15 min")

                lessons.append(lesson_data)

        modules.append({
            "id": module_data["id"],
            "title": module_data["title"],
            "lessons": lessons
        })

    return modules



PYTHON_MODULES = [
    {
        "id": "python-basics",
        "title": "Module 1: Python Basics",
        "lesson_ids": [
            "python-introduction",
            "python-variables",
            "python-arithmetic"
        ]
    },
    {
        "id": "python-conditions",
        "title": "Module 2: Conditional Statements",
        "lesson_ids": [
            "python-if-else"
        ]
    },
    {
        "id": "python-loops",
        "title": "Module 3: Loops",
        "lesson_ids": [
            "python-for-loop",
            "python-while-loop"
        ]
    },
    {
        "id": "python-functions",
        "title": "Module 4: Functions",
        "lesson_ids": [
            "python-function-basics"
        ]
    },
    {
        "id": "python-collections",
        "title": "Module 5: Python Collections",
        "lesson_ids": [
            "python-lists",
            "python-tuples",
            "python-sets",
            "python-dictionaries"
        ]
    },
    {
        "id": "python-oops",
        "title": "Module 6: Object-Oriented Programming",
        "lesson_ids": [
            "python-oops-classes",
            "python-oops-encapsulation",
            "python-oops-polymorphism",
            "python-oops-abstraction"
        ]
    },
    {
        "id": "python-libraries",
        "title": "Module 7: Python Libraries",
        "lesson_ids": [
            "python-numpy",
            "python-pandas"
        ]
    },
    {
        "id": "python-backend",
        "title": "Module 8: Python Backend Development",
        "lesson_ids": [
            "python-rest-api",
            "python-fastapi",
            "python-flask",
            "python-sqlalchemy",
            "python-jwt-authentication",
            "python-sql-database-fundamentals"
        ]
    }
]


DSA_MODULES = [
    {
        "id": "dsa-complexity",
        "title": "Module 1: Complexity Analysis and Recursion",
        "lesson_ids": [
            "dsa-time-complexity",
            "dsa-space-complexity",
            "dsa-recursion"
        ]
    },
    {
        "id": "dsa-arrays",
        "title": "Module 2: Arrays and Array Techniques",
        "lesson_ids": [
            "dsa-array-basics",
            "dsa-prefix-sum",
            "dsa-sliding-window",
            "dsa-two-pointers"
        ]
    },
    {
        "id": "dsa-strings-hashing",
        "title": "Module 3: Strings and Hashing",
        "lesson_ids": [
            "dsa-strings-basics",
            "dsa-hashmap"
        ]
    },
    {
        "id": "dsa-search-sorting",
        "title": "Module 4: Searching and Sorting",
        "lesson_ids": [
            "dsa-binary-search",
            "dsa-sorting"
        ]
    },
    {
        "id": "dsa-linear-structures",
        "title": "Module 5: Linked Lists, Stacks and Queues",
        "lesson_ids": [
            "dsa-linked-list",
            "dsa-stack-queue"
        ]
    },
    {
        "id": "dsa-trees-graphs",
        "title": "Module 6: Trees, Graphs and Tries",
        "lesson_ids": [
            "dsa-binary-tree",
            "dsa-graphs",
            "dsa-tries"
        ]
    },
    {
        "id": "dsa-algorithmic-techniques",
        "title": "Module 7: Advanced Problem-Solving Techniques",
        "lesson_ids": [
            "dsa-greedy",
            "dsa-backtracking",
            "dsa-dynamic-programming",
            "dsa-bit-manipulation"
        ]
    }
]


LEARNING_PATHS = [
    {
        "id": "python-foundations",
        "title": "Python Foundations",
        "description": "Learn Python programming, libraries and backend development from scratch.",
        "level": "Beginner to Intermediate",
        "icon": "Py",
        "modules": build_modules(
            PYTHON_FOUNDATIONS,
            PYTHON_MODULES
        )
    },
    {
        "id": "dsa-track",
        "title": "Data Structures & Algorithms",
        "description": "Master problem-solving and essential DSA concepts.",
        "level": "Beginner to Advanced",
        "icon": "⌘",
        "modules": build_modules(
            DSA_TRACK,
            DSA_MODULES
        )
    }
]


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def find_lesson(lesson_id):

    for path in LEARNING_PATHS:

        for module in path["modules"]:

            for lesson in module["lessons"]:

                if lesson["id"] == lesson_id:
                    return path, module, lesson

    return None, None, None


def get_user_progress(db, user_id):

    return db.query(UserLessonProgress).filter(
        UserLessonProgress.user_id == user_id
    ).all()


def calculate_path_progress(path, progress_records):

    completed_ids = {
        record.lesson_id
        for record in progress_records
        if record.completed
    }

    total = sum(
        len(module["lessons"])
        for module in path["modules"]
    )

    completed = sum(
        1
        for module in path["modules"]
        for lesson in module["lessons"]
        if lesson["id"] in completed_ids
    )

    percentage = round(
        (completed / total) * 100
    ) if total else 0

    return {
        "completed_lessons": completed,
        "total_lessons": total,
        "percentage": percentage
    }


# ==========================================
# GET ALL LEARNING PATHS
# ==========================================

@router.get("/paths")
def get_learning_paths(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    progress_records = get_user_progress(
        db,
        current_user.id
    )

    result = []

    for path in LEARNING_PATHS:

        path_data = {
            "id": path["id"],
            "title": path["title"],
            "description": path["description"],
            "level": path["level"],
            "icon": path["icon"],
            "modules": []
        }

        for module in path["modules"]:

            module_data = {
                "id": module["id"],
                "title": module["title"],
                "lessons": []
            }

            for lesson in module["lessons"]:

                lesson_progress = next(
                    (
                        record
                        for record in progress_records
                        if record.lesson_id == lesson["id"]
                        and record.completed
                    ),
                    None
                )

                module_data["lessons"].append({
                    "id": lesson["id"],
                    "title": lesson["title"],
                    "duration": lesson["duration"],
                    "completed": lesson_progress is not None
                })

            path_data["modules"].append(module_data)

        path_data["progress"] = calculate_path_progress(
            path,
            progress_records
        )

        result.append(path_data)

    return {
        "success": True,
        "paths": result
    }


# ==========================================
# GET SINGLE LESSON
# ==========================================

@router.get("/lessons/{lesson_id}")
def get_lesson(
    lesson_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    path, module, lesson = find_lesson(lesson_id)

    if not lesson:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found"
        )

    progress = db.query(UserLessonProgress).filter(
        UserLessonProgress.user_id == current_user.id,
        UserLessonProgress.lesson_id == lesson_id
    ).first()

    return {
        "success": True,
        "path": {
            "id": path["id"],
            "title": path["title"]
        },
        "module": module["title"],
        "lesson": lesson,
        "completed": progress.completed if progress else False
    }


# ==========================================
# COMPLETE LESSON
# ==========================================

@router.post("/lessons/{lesson_id}/complete")
def complete_lesson(
    lesson_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    path, module, lesson = find_lesson(lesson_id)

    if not lesson:
        raise HTTPException(
            status_code=404,
            detail="Lesson not found"
        )

    progress = db.query(UserLessonProgress).filter(
        UserLessonProgress.user_id == current_user.id,
        UserLessonProgress.lesson_id == lesson_id
    ).first()

    if progress and progress.completed:

        return {
            "success": True,
            "already_completed": True,
            "message": "You have already completed this lesson.",
            "xp_earned": 0,
            "total_xp": current_user.xp
        }

    if not progress:

        progress = UserLessonProgress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            completed=True,
            completed_at=datetime.utcnow()
        )

        db.add(progress)

    else:

        progress.completed = True
        progress.completed_at = datetime.utcnow()

    current_user.xp = (
        (current_user.xp or 0) + XP_PER_LESSON
    )

    current_user.level = (
        current_user.xp // 100
    ) + 1

    db.commit()
    db.refresh(current_user)

    return {
        "success": True,
        "already_completed": False,
        "message": "Lesson completed successfully!",
        "xp_earned": XP_PER_LESSON,
        "total_xp": current_user.xp,
        "level": current_user.level
    }


# ==========================================
# GET USER LEARNING SUMMARY
# ==========================================

@router.get("/progress")
def get_learning_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    records = get_user_progress(
        db,
        current_user.id
    )

    completed_ids = [
        record.lesson_id
        for record in records
        if record.completed
    ]

    total_lessons = sum(
        len(module["lessons"])
        for path in LEARNING_PATHS
        for module in path["modules"]
    )

    completed_count = sum(
        1 for lesson_id in completed_ids
        if find_lesson(lesson_id)[2] is not None
    )

    return {
        "success": True,
        "completed_lessons": completed_count,
        "total_lessons": total_lessons,
        "percentage": round(
            (completed_count / total_lessons) * 100
        ) if total_lessons else 0,
        "completed_lesson_ids": completed_ids,
        "xp": current_user.xp,
        "level": current_user.level
    }
