from typing import List
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from App.Database.schemas import User

UserModel = sqlalchemy_to_pydantic(User)