from pydantic import BaseModel
from datetime import datetime
from typing import List, Union


class Book(BaseModel):
    book_id: int
    user_id: int
    book_name: str
    book_author: str
    words: List[Word]

    class Config:
        orm_mode = True


class Goal(BaseModel):
    goal_id: int
    goal_level: str
    date: datetime


class User_level(BaseModel):
    user_level_id: int
    current_level: str


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    goal_id: int
    user_level_id: int
    user_name: str
    native_language: str
    books: List[Book]
    goal: Goal
    user_level: User_level

    class Config:
        orm_mode = True
