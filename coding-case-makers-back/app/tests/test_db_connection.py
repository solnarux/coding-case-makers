import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.data.database import get_db


@pytest.fixture(scope="module")
def db_session() -> Session:
    """Create a new database session for a test."""
    db_generator = get_db()
    db = next(db_generator)
    yield db
    db_generator.close()


def test_db_connection(db_session):
    """Test the database connection by executing a simple query."""
    result = db_session.execute(text("SELECT 1"))
    assert result.fetchone() == (1,)
