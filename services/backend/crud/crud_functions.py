from random import randint

from sqlalchemy.orm import Session
from typing import List, Dict, Tuple
from models.model import User, Book, User_word, DB_word
from schemas.schema import UserCreate, UserUpdate, DBWordCreate, DBWord, \
    UserWord, UserWordCreate, BookCreate


def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# # TODO: use it for list of books ??!
# def get_book(db: Session, book_id: int):
#     return db.query(Book).filter(Book.book_id == book_id).first()
#
# # TODO: use it for list of books ??!
# def get_books(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Book).offset(skip).limit(limit).all()


def create_user_word(db: Session, user_word: UserWordCreate) -> UserWord:
    user_word_obj = User_word(**user_word.dict())
    db.add(user_word_obj)
    db.commit()
    db.refresh(user_word_obj)
    return user_word_obj

#
def get_user_words_by_book(db: Session, book_id: int):
    return db.query(User_word).filter(User_word.book_id == book_id).all()


def get_random_user_book(db: Session, user_id: int) -> Book:
    books = db.query(Book).filter(Book.user_id == user_id).all()
    if len(books) == 0:
        raise Exception("No book in DB")  # TODO: an exception to front end
    elif len(books) == 1:
        return books[0]
    else:
        book = books[randint(0, len(books)-1)]
        return book


def get_unknown_user_word_by_book_id(db: Session, book_id: int) -> DB_word:
    user_words = db.query(User_word).filter(User_word.book_id == book_id).all()  # and not User_word.is_known
    # TODO: user_words is empty and also the condition with User_word.is_known should be added
    if len(user_words) == 0:
        raise Exception("No user words in DB or every word has been already learned")  # TODO: an exception to front end
        #return book_id
    elif len(user_words) == 1:
        return user_words[0]
    else:
        user_word = user_words[randint(0, len(user_words)-1)]
        return db.query(DB_word).filter(DB_word.en_word == user_word.en_word).first()


def get_books_by_user_id(db: Session, user_id: int) -> List[Book]:
    return db.query(Book).filter(Book.user_id == user_id).all()


def get_db_word_by_en_word(db: Session, en_word: str) -> DB_word:
    return db.query(DB_word).filter(DB_word.en_word == en_word).first()


def get_user_profile(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def change_user_word_status(db: Session, book_id: int, en_word: str):
    user_words = db.query(User_word).filter(Book.book_id == book_id).all()
    for user_word in user_words:
        if user_word.en_word == en_word:
            user_word.is_known = True
            db.commit()
            break


def update_user_info(db: Session, user_id: int, goal_level: str, user_name: str, user_level: str, native_language: str):
    user = db.query(User).filter(User.id == user_id).first()
    user.goal_level = goal_level
    user.user_name = user_name
    user.user_level = user_level
    user.native_language = native_language

    db.commit()
