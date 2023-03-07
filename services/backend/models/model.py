from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

# from db.base_class import Base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user_table'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    current_num_level: Mapped[int] = mapped_column()
    goal_level: Mapped[str] = mapped_column(String(2))
    user_level: Mapped[str] = mapped_column(String(3))
    user_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    native_language: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))
    frame_path: Mapped[str] = mapped_column(String(120))

    books: Mapped[List["Book"]] = relationship()


class DB_word(Base):
    __tablename__ = 'db_word_table'

    en_word: Mapped[str] = mapped_column(String(50), primary_key=True)
    word_level: Mapped[str] = mapped_column(String(2))
    uk_word: Mapped[str] = mapped_column(String(50))

    user_word: Mapped['User_word'] = relationship(back_populates='db_word')


class User_word(Base):
    __tablename__ = 'user_word_table'

    word_id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('book_table.book_id'))
    en_word: Mapped[str] = mapped_column(String(50), ForeignKey('db_word_table.en_word'))
    is_known: Mapped[bool]

    db_word: Mapped["DB_word"] = relationship(back_populates='user_word')


class Book(Base):
    __tablename__ = 'book_table'

    book_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_table.user_id'))
    book_title: Mapped[str] = mapped_column(String(50))
    book_author: Mapped[str] = mapped_column(String(50))

    words: Mapped[List["User_word"]] = relationship()
