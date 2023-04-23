from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str
    email: str
    native_language: str
    goal_level: str
    user_level: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    current_num_level: int
    frame_path: Optional[str] = None
    books: List["Book"] = []

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    user_name: Optional[str] = None
    email: Optional[str] = None
    native_language: Optional[str] = None
    password: Optional[str] = None
    frame: Optional[str] = None


class DBWordCreate(BaseModel):
    en_word: str


class DBWord(DBWordCreate):
    word_level: Optional[str]
    uk_word: Optional[str]

    # class Config:
    #     orm_mode = True


class UserWordBase(BaseModel):
    en_word: str
    is_known: bool


class UserWordCreate(UserWordBase):
    book_id: int


class UserWord(UserWordBase):
    word_id: int
    db_word: Optional[DBWord]

    # class Config:
    #     orm_mode = True


class BookBase(BaseModel):
    book_title: str
    book_author: str


class BookCreate(BookBase):
    user_id: int


class Book(BookBase):
    book_id: int
    words: List[UserWord] = []

    # class Config:
    #     orm_mode = True