from fastapi import Depends, UploadFile, File, APIRouter, Request
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from dependencies import get_db

from routers_logic.send_book import send_book

router = APIRouter()


@router.post("/sendbook")
def send_book_endpoint(request: Request, level: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        jwt = request.headers['Cookie'].split('=')[1]
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    return send_book(user_id=user_id, level=level, file=file, db=db)
