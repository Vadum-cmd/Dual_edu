from fastapi import Depends, APIRouter, Request, HTTPException, status
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from dependencies import get_db
from crud.crud_functions import get_user_profile, update_user_info
from schemas.schema import SettingsUpdate

router = APIRouter()

@router.get("/resetpassword")
def get_settings(token: str, request: Request):
    return {"token": token}
