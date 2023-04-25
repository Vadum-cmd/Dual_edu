from fastapi import FastAPI, Depends, APIRouter, Header, Request, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated

from auth.jwt_decoder import decode_user
from dependencies import get_db
from crud.crud_functions import get_user_profile


router = APIRouter()

@router.get("/profile")
def get_profile_info(request: Request, db: Session = Depends(get_db)):
    try:
        jwt = request.headers['Cookie'].split('=')[1]
        user_id = int(decode_user(jwt)['sub'])
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            # headers={"WWW-Authenticate": "Basic"},
        )
        # return None

    return get_user_profile(db=db, user_id=user_id)


