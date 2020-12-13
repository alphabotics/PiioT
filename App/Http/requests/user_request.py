from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    id: int
    email: str
    first_name: str