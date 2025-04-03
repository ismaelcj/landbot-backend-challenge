import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.shared.infrastructure.api.main import app
from src.shared.infrastructure.persistence.database import SQLBase, get_db


@pytest.fixture
def test_db():
    # Create an in-memory SQLite database for testing
    # We still use SQLite for tests for simplicity
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Create all tables
    SQLBase.metadata.create_all(bind=engine)

    # Create a test database session
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        SQLBase.metadata.drop_all(bind=engine)


@pytest.fixture
def client(test_db):
    # Override the get_db dependency to use the test database
    def override_get_db():
        try:
            yield test_db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    # Reset the dependency override
    app.dependency_overrides = {}
