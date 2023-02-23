from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
# from crud.crud import

app = FastAPI()
