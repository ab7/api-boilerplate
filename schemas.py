from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    pass


class User(BaseModel):
    id: int
    username: str
    email: str
    enabled: bool

    class Config:
        orm_mode = True
