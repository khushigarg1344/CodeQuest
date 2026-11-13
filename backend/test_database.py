from database.database import SessionLocal
from database.models import User, Problem, Badge


db = SessionLocal()


print("\n========== DATABASE TEST ==========\n")


# Test Problems
problems = db.query(Problem).all()

print("Problems:")
for problem in problems:
    print(
        f"ID: {problem.id} | "
        f"Title: {problem.title} | "
        f"Topic: {problem.topic} | "
        f"XP: {problem.xp_reward}"
    )


# Test Badges
badges = db.query(Badge).all()

print("\nBadges:")
for badge in badges:
    print(
        f"ID: {badge.id} | "
        f"Name: {badge.name} | "
        f"Icon: {badge.icon}"
    )


# Test Users
users = db.query(User).all()

print("\nUsers:")
print(f"Total users: {len(users)}")


print("\n==================================")
print("DATABASE TEST COMPLETED")
print("==================================\n")


db.close()