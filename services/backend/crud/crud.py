from sqlalchemy.orm import Session
from typing import List
from ..models.model import User, User_level, Word, Book, Goal
from ..schemas.new_schema import UserCreate, UserUpdate, User_levelCreate, User_levelUpdate, WordCreate, WordUpdate, BookCreate, BookUpdate, GoalCreate, GoalUpdate

#Returns a user with the specified user_id.
def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.user_id == user_id).first()

#Returns a list of users with optional pagination using the skip and limit parameters.
def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()

#Creates a new user with the provided data and returns the newly created user.
def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Updates a user with the specified user_id with the provided data and returns the updated user.
def update_user(db: Session, user: User, user_update: UserUpdate) -> User:
    for field, value in user_update:
        setattr(user, field, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

#Deletes a user with the specified user_id.
def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()

#Returns a user level with the specified user_level_id.
def get_user_level(db: Session, user_level_id: int) -> User_level:
    return db.query(User_level).filter(User_level.user_level_id == user_level_id).first()


#Creates a new user level with the provided data and returns the newly created user level.
def create_user_level(db: Session, user_level: User_levelCreate) -> User_level:
    db_user_level = User_level(**user_level.dict())
    db.add(db_user_level)
    db.commit()
    db.refresh(db_user_level)
    return db_user_level

#Updates a user level with the specified user_level_id with the provided data and returns the updated user level.
def update_user_level(db: Session, user_level: User_level, user_level_update: User_levelUpdate) -> User_level:
    for field, value in user_level_update:
        setattr(user_level, field, value)
    db.add(user_level)
    db.commit()
    db.refresh(user_level)
    return user_level

#Deletes a user level with the specified user_level_id.
def delete_user_level(db: Session, user_level: User_level) -> None:
    db.delete(user_level)
    db.commit()


def create_goal(db: Session, goal: GoalCreate):
    db_goal = Goal(goal_level=goal.goal_level, date=goal.date, user_id=goal.user_id)
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal


def get_goal(db: Session, goal_id: int):
    return db.query(Goal).filter(Goal.goal_id == goal_id).first()


def update_goal(db: Session, goal_id: int, goal: GoalUpdate):
    db_goal = db.query(Goal).filter(Goal.goal_id == goal_id).first()
    if db_goal:
        for key, value in goal.dict(exclude_unset=True).items():
            setattr(db_goal, key, value)
        db.commit()
        db.refresh(db_goal)
    return db_goal


def delete_goal(db: Session, goal_id: int):
    db_goal = db.query(Goal).filter(Goal.goal_id == goal_id).first()
    if db_goal:
        db.delete(db_goal)
        db.commit()
    return db_goal

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.book_id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.book_id == book_id).first()
    for field, value in book:
        setattr(db_book, field, value) if value else None
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.book_id == book_id).first()
    db.delete(db_book)
    db.commit()

def create_word(db: Session, word: WordCreate):
    db_word = Word(**word.dict())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word


def get_word(db: Session, word_id: int):
    return db.query(Word).filter(Word.word_id == word_id).first()


def get_words(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Word).offset(skip).limit(limit).all()


def update_word(db: Session, word_id: int, word: WordUpdate):
    db_word = db.query(Word).filter(Word.word_id == word_id).first()
    for field, value in word:
        setattr(db_word, field, value)
    db.commit()
    db.refresh(db_word)
    return db_word


def delete_word(db: Session, word_id: int):
    db_word = db.query(Word).filter(Word.word_id == word_id).first()  
    db.delete(db_word)
    db.commit()
        
