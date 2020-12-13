import pathlib
import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

# Load environtment from .env
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
APP_PATH = "%s" % Path(CURRENT_DIR).parent
env_path = "%s/.env" % Path(CURRENT_DIR).parent

load_dotenv(dotenv_path=env_path, verbose=True)


class Settings(BaseSettings):
    APP_PATH: str = APP_PATH
    PROJECT_NAME: str = "FastAdmin"
    API_ADMIN_PREFIX: str = "/api/admin"
    API_V1_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days
    SQLALCHEMY_DATABASE_URI: str = "mysql+pymysql://%s:%s@%s:%s/%s" % (
        os.getenv('MYSQL_USERNAME'),
        os.getenv('MYSQL_PASSWORD'),
        os.getenv('MYSQL_HOST'),
        os.getenv('MYSQL_PORT'),
        os.getenv('MYSQL_DB')
    )

    class Config:
        case_sensitive = True


settings = Settings()
print("settings", settings)
