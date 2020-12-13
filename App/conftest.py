import sys, os
# Append App pakage to use in pytest
sys.path.append(os.getcwd())

import App
import pytest
from App.Config.config import settings
from App.Database.database import SessionLocal


@pytest.fixture
def db_session(request):
    session = SessionLocal()
    return session
