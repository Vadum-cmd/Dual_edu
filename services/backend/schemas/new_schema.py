from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):   
    user_name: str
    email: str
    native_language: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    goal_id: Optional[int] = None
    user_level_id: Optional[int] = None
    frame: Optional[str] = None
    books: List["Book"] = []

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    user_name: Optional[str] = None
    email: Optional[str] = None
    native_language: Optional[str] = None
    password: Optional[str] = None
    frame: Optional[str] = None


class User_levelBase(BaseModel):
    current_level: str


class User_levelCreate(User_levelBase):
    pass


class User_level(User_levelBase):
    user_level_id: int
    user_lvl: User

    class Config:
        orm_mode = True


class User_levelUpdate(User_levelBase):
    pass


class GoalBase(BaseModel):
    goal_level: str
    date: Optional[datetime] = None


class GoalCreate(GoalBase):
    user_id: int


class Goal(GoalBase):
    goal_id: int
    user: User

    class Config:
        orm_mode = True


class GoalUpdate(GoalBase):
    pass

class DBWordBase(BaseModel):
    en_word: str
    word_level: Optional[str]
    uk_word: Optional[str]


class DBWordCreate(DBWordBase):
    pass


class DBWord(DBWordBase):
    class Config:
        orm_mode = True

class DBWord(DBWordBase):
    pass

class UserWordBase(BaseModel):
    en_word: str
    is_known: bool

class UserWordCreate(UserWordBase):
    book_id: int

class UserWord(UserWordBase):
    word_id: int
    db_word: Optional[DBWord]
    class Config:
        orm_mode = True

class UserWordUpdate(UserWordBase):
    pass

class BookBase(BaseModel):
    book_title: str
    book_author: str


class BookCreate(BookBase):
    user_id: int


class Book(BookBase):
    book_id: int
    user_id: int
    words: List[UserWord] = []

    class Config:
        orm_mode = True


class BookUpdate(BookBase):
    pass

# class WordBase(BaseModel):
#     word_level: str
#     uk_word: str
#     en_word: str


# class WordCreate(WordBase):
#     book_id: int


# class Word(WordBase):
#     word_id: int
#     book_id: int

#     class Config:
#         orm_mode = True


# class WordUpdate(WordBase):
#     pass