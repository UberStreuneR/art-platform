from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class UserInDB(User):
    hashed_password: str


class UserCreate(BaseModel):
    username: str
    password: str


class UserUpdate(BaseModel):
    pass
