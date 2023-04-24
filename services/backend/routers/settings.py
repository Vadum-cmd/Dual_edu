from fastapi import FastAPI, Depends, APIRouter, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from dependencies import get_db
from crud.crud_functions import get_user_profile, update_user_info
from schemas.schema import SettingsUpdate, JWT

router = APIRouter()

@router.get("/settings")
def get_settings(request: Request, db: Session = Depends(get_db)):
    jwt = request.headers['Cookie'].split('=')[1]

    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    return get_user_profile(db=db, user_id=user_id)


@router.post("/settings")
def post_settings( settingsUpdate: SettingsUpdate,request: Request, db: Session = Depends(get_db)):
    jwt = request.headers['Cookie'].split('=')[1]


    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    update_user_info(db=db, user_id=user_id, goal_level=settingsUpdate.goal_level, user_name=settingsUpdate.user_name, user_level=settingsUpdate.user_level, native_language=settingsUpdate.native_language)

    return get_user_profile(db=db, user_id=user_id)
