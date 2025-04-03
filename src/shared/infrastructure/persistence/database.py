from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
from sqlalchemy.orm import Session

from src.shared.infrastructure.config import settings

engine = create_engine(
    settings.DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SQLBase = declarative_base()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
