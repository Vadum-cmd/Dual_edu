from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from auth.db import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from fastapi_users import fastapi_users, FastAPIUsers
from routers.vocabulary import router as vocabulary_router
from routers.sendbook import router as sendbook_router
from routers.profile import router as profile_router
from routers.settings import router as settings_router
from routers.home import router as home_router
from routers.words_test import router as words_test_router
# from routers.login_signup import router as login_signup_router
from routers.download_file import router as download_file_router


app = FastAPI()

app.include_router(vocabulary_router)
app.include_router(sendbook_router)
app.include_router(profile_router)
app.include_router(settings_router)
app.include_router(words_test_router)
app.include_router(download_file_router)
app.include_router(home_router)

fastapi_users_ = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users_.get_auth_router(auth_backend),
    prefix="",
    tags=["auth"],
)

app.include_router(
    fastapi_users_.get_register_router(UserRead, UserCreate),
    prefix="",
    tags=["auth"],
)

# TODO: reset_password_router
# https://fastapi-users.github.io/fastapi-users/10.4/configuration/routers/reset/
app.include_router(
    fastapi_users_.get_verify_router(UserRead),
    prefix="",
    tags=["auth"],
)

app.include_router(
    fastapi_users_.get_reset_password_router(),
    prefix="",
    tags=["auth"],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)



