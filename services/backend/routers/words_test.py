from fastapi import FastAPI, Depends, APIRouter, Request
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from dependencies import get_db
from crud.crud_functions import get_db_word_by_en_word, change_user_word_status, get_random_user_book, \
    get_unknown_user_word_by_book_id
from routers_logic.words_test_game import check_user_answer, get_random_word

router = APIRouter()


@router.get("/test")
def get_word_for_test_endpoint(request: Request, db: Session = Depends(get_db)):
    try:
        jwt = request.headers['Cookie'].split('=')[1]
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    return get_random_word(user_id=user_id, db=db)


@router.post("/test")
def check_word(request: Request, en_word: str, answer: str, book_id: int, db: Session = Depends(get_db)):
    try:
        jwt = request.headers['Cookie'].split('=')[1]
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    return check_user_answer(en_word=en_word, answer=answer, book_id=book_id, db=db)

