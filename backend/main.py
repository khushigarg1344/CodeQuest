import os
from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import Base, engine
from database import models  # ensure SQLAlchemy models are registered before create_all
from database.seed import seed_database
from routes.problems import router as problems_router
from routes.auth import router as auth_router
from routes.users import router as users_router
from routes.submissions import router as submissions_router
from routes.badges import router as badges_router
from routes.ai import router as ai_router
from routes import learning

app = FastAPI(
    title="CodeQuest API",
    description="Backend for the CodeQuest gamified coding and DSA learning platform.",
    version="1.0.0",
)

origins = os.getenv("FRONTEND_ORIGINS", "http://127.0.0.1:5173,http://localhost:5173,http://127.0.0.1:5174,http://localhost:5174").split(",")
app.add_middleware(
    CORSMiddleware, allow_origins=[origin.strip() for origin in origins],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
try:
    seed_database()
except Exception as exc:
    # Keep the API available if the seed data needs attention; details appear in terminal.
    print(f"CodeQuest seed warning: {exc}")

app.include_router(problems_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(submissions_router)
app.include_router(ai_router)
app.include_router(learning.router)
app.include_router(badges_router)
@app.get("/")
def home():
    return {"message": "Welcome to CodeQuest API!", "status": "running", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}

@app.get("/api/v1")
def api_info():
    return {"name": "CodeQuest", "version": "1.0.0", "features": ["DSA practice", "Gamification", "AI Tutor", "Code execution", "Progress tracking"]}
