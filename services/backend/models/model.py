from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

# from db.base_class import Base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    # user_id: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    current_num_level: Mapped[int] = mapped_column()
    goal_level: Mapped[str] = mapped_column(String(2))
    user_level: Mapped[str] = mapped_column(String(3))
    user_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    native_language: Mapped[str] = mapped_column(String(50))
    frame_path: Mapped[str] = mapped_column(String(120))

    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    books: Mapped[List["Book"]] = relationship()


class DB_word(Base):
    __tablename__ = 'db_word'

    en_word: Mapped[str] = mapped_column(String(50), primary_key=True)
    word_level: Mapped[str] = mapped_column(String(2))
    uk_word: Mapped[str] = mapped_column(String(90))
    es_word: Mapped[str] = mapped_column(String(90))
    word_type: Mapped[str] = mapped_column(String(20))

    user_word: Mapped['User_word'] = relationship(back_populates='db_word')


class User_word(Base):
    __tablename__ = 'user_word'

    word_id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('book.book_id'))
    en_word: Mapped[str] = mapped_column(String(50), ForeignKey('db_word.en_word'))
    is_known: Mapped[bool]

    db_word: Mapped["DB_word"] = relationship(back_populates='user_word')


class Book(Base):
    __tablename__ = 'book'

    book_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    book_title: Mapped[str] = mapped_column(String(50))
    book_author: Mapped[str] = mapped_column(String(50))

    words: Mapped[List["User_word"]] = relationship()
