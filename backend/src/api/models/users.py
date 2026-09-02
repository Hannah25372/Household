from pydantic import BaseModel
from database.enums import Role


class UserCreate(BaseModel):
    name: str
    email: str
    role: Role


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: Role