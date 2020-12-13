from pydantic import BaseModel
from typing import Optional


class UserCreateRequest(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    job_title: str = None
    phone: str = None


class UserUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    job_title: Optional[str] = None
    phone: Optional[str] = None