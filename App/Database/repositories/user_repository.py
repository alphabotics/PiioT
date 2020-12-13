from sqlalchemy.orm import Session

from App.Database.repositories.base_repository import BaseRepository
from App.Database.schemas import User
from App.Http.requests.user_request import UserCreateRequest
from App.Database.database import SessionLocal

from App.models.user import User

class UserRepository(BaseRepository):

    _model = User
