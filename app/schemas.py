from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class TodoBase(BaseModel):
    title: str
    description: str | None = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    completed: bool


class TodoResponse(TodoBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime
    owner_id: int

    class Config:
        orm_mode = True
