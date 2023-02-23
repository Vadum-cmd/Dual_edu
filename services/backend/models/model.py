from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import List
from ..db.session import Base

metadata = Base.metadata

class User(Base):

    __tablename__ = 'user_table'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    goal_id:Mapped[int] = mapped_column(ForeignKey('goal_table.goal_id'))
    user_level_id:Mapped[int] = mapped_column(ForeignKey('user_level_table.user_level_id'))
    password:Mapped[int] =  mapped_column(String(50))
    user_name:Mapped[str] = mapped_column(String(50))
    email:Mapped[str] = mapped_column(String(50))
    frame:Mapped[str] = mapped_column(String(120))
    native_language:Mapped[str] = mapped_column(String(50))
    
    books: Mapped[List["Book"]] = relationship()
    goal: Mapped["Goal"] = relationship(back_populates="user")
    user_level:Mapped["User_level"] = relationship(back_populates="user_lvl")

class User_level(Base):

    __tablename__ = 'user_level_table'

    user_level_id:Mapped[int] = mapped_column(primary_key=True)
    current_level:Mapped[str] = mapped_column(String(2))
    
    user_lvl: Mapped["User"] = relationship(uselist=False,back_populates='user_level')

class Goal(Base):

    __tablename__ = 'goal_table'

    goal_id: Mapped[int] = mapped_column(primary_key=True)
    goal_level: Mapped[str] = mapped_column(String(2))
    date:Mapped[datetime]
    
    user: Mapped["User"] = relationship(uselist=False,back_populates='goal')
   
class Word(Base):

    __tablename__ = 'word_table'

    word_id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('book_table.book_id'))
    word_level: Mapped[str] = mapped_column(String(2))
    uk_word:Mapped[str] = mapped_column(String(50))
    en_word:Mapped[str] = mapped_column(String(50))

class Book(Base):

    __tablename__ = 'book_table'

    book_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_table.user_id'))
    book_name:Mapped[str] = mapped_column(String(50))
    book_author:Mapped[str]  = mapped_column(String(50))
    
    words: Mapped[List["Word"]] = relationship()
    

