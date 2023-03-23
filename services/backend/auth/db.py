from typing import AsyncGenerator, List

import sqlalchemy
from fastapi import Depends
from sqlalchemy import Boolean, String, Integer

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

DATABASE_URL = "mysql+asyncmy://root:uTnw0PIh65_!@127.0.0.1:3306/dual_edu"  # TODO : async stated after "mysql:..."

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    user_id: Mapped[int] = mapped_column(primary_key=True)
    current_num_level: Mapped[int] = mapped_column()
    goal_level: Mapped[str] = mapped_column(String(2))
    user_level: Mapped[str] = mapped_column(String(3))
    user_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    native_language: Mapped[str] = mapped_column(String(50))
    # password: Mapped[str] = mapped_column(String(50))
    frame_path: Mapped[str] = mapped_column(String(120))

    #books: Mapped[List["Book"]] = relationship()  # TODO: ?!
    # TODO: foreign key might be different

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



engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
