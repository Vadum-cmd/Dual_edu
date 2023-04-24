from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from crud.crud_functions import get_books_by_user_id
from dependencies import get_db
from routers_logic.get_vocabulary import get_vocabulary

router = APIRouter()


@router.get("/books")
def get_books(request: Request, db: Session = Depends(get_db)):
    jwt = request.headers['Cookie'].split('=')[1]

    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    return get_books_by_user_id(user_id=user_id, db=db)