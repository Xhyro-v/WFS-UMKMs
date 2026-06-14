from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import DATABASE_URL_TEST

engine = create_engine(
    DATABASE_URL_TEST, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()