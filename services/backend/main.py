from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.vocabulary import router as vocabulary_router
from routers.sendbook import router as sendbook_router
from routers.profile import router as profile_router
from routers.settings import router as settings_router
from routers.words_test import router as words_test_router
# from routers.login_signup import router as login_signup_router
from routers.download_file import router as download_file_router


app = FastAPI()

app.include_router(vocabulary_router)
app.include_router(sendbook_router)
app.include_router(profile_router)
app.include_router(settings_router)
app.include_router(words_test_router)
# app.include_router(login_signup_router)
app.include_router(download_file_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

