from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_user_profile


router = APIRouter()

@router.get("/settings")
def get_settings(user_id: int, db: Session = Depends(get_db)):
    return get_user_profile(db=db, user_id=user_id)
