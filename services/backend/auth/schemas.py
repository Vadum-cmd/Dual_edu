from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):

    id: int
    email: str
    user_name: str
    native_language: str
    goal_level: str
    user_level: str
    frame_path: str
    current_num_level: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    user_name: str
    native_language: str
    goal_level: str
    user_level: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


# class UserUpdate(schemas.BaseUserUpdate):
#     pass