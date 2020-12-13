from sqlalchemy.orm import Session

from App.Database.repositories.base_repository import BaseRepository
from App.Database.schemas import User
from App.Http.requests.user_request import UserCreateRequest
from App.Database.database import SessionLocal

from App.models.user import User

class UserRepository(BaseRepository):

    def __init__(self):
        self.db = SessionLocal()

    def paginate(self, limit: int=10, offset: int=0):
        users = User.paginate(limit)
        return self.formatted_paginate(users)

    def first(db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    def find_where(db: Session, email: str):
        return 'find_where'
        # return db.query(User).filter(User.email == email).first()

    def create(db: Session, user: UserCreateRequest):
        db_user = User(email=user.email, first_name=user.first_name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(db: Session, user: User):
        return 'Updated user'

    def delete(db: Session, id: int):
        return 'Deleted user'
