from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# .env の DATABASE_URL を取得（デフォルトは SQLite）
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# SQLite なら check_same_thread を設定、PostgreSQL ならそのまま
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)  # PostgreSQL の場合は `connect_args` をなくす

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
