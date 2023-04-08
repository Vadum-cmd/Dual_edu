from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from dependencies import get_db
from crud.crud_functions import get_db_word_by_en_word, change_user_word_status, get_random_user_book, \
    get_unknown_user_word_by_book_id

router = APIRouter()


@router.get("/test")
def get_random_word(jwt: str, db: Session = Depends(get_db)):
    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    book = get_random_user_book(db=db, user_id=user_id)
    word = get_unknown_user_word_by_book_id(db=db, book_id=book.book_id)
    print(word)
    return {"word": word, "book_id": book.book_id} #.en_word


@router.post("/test")
def check_word(jwt: str, en_word: str, answer: str, book_id: int, db: Session = Depends(get_db)):
    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    if answer.lower() == get_db_word_by_en_word(db=db, en_word=en_word).uk_word.lower():
        change_user_word_status(db=db, book_id=book_id, en_word=en_word)
        return {"result": True}
    else:
        return {"result": False, "correct_answer": get_db_word_by_en_word(db=db, en_word=en_word).uk_word}

