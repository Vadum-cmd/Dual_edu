from fastapi import FastAPI, Depends, APIRouter, Request
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from dependencies import get_db
from crud.crud_functions import get_user_profile


router = APIRouter()

@router.get("/home")
def get_user_level(jwt: str, request: Request, db: Session = Depends(get_db)):
    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    return {"user_level": get_user_profile(db=db, user_id=user_id).user_level}
