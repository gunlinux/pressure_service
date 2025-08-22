from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    id: int
    telegram_nickname: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    registration_data: datetime

    class Config:
        from_orm = True
