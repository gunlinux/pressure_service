from unittest.mock import patch
import pytest
from app.db.session import get_db
from sqlalchemy.exc import SQLAlchemyError
from app.db import session

def test_get_db_exception():
    with pytest.raises(SQLAlchemyError):
        with patch('app.db.session.SessionLocal', side_effect=SQLAlchemyError()):
            next(get_db())

def test_session_creation():
    assert session.engine is not None
    assert session.SessionLocal is not None
