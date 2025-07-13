from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Generator
from sqlalchemy.orm import Session


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
