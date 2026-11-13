import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# Set DATABASE_URL in backend/.env to use PostgreSQL. SQLite is a local fallback
# so the app can still start before PostgreSQL is installed/configured.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./codequest.db"
)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
