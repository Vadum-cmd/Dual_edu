from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_user_prof
from main import app


router = APIRouter()

@app.router("/profile")
def get_profile_info(user_id: int, db: Session = Depends(get_db)):
    return get_user_prof(db=db, user_id=user_id)

