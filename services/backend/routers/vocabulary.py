from typing import Set

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from dependencies import get_db
from crud.crud_functions import get_books_by_user_id
from crud.crud_functions import get_user_words_by_book, get_db_word_by_en_word



router = APIRouter()


@router.get("/vocabulary")
def get_vocabulary(jwt: str, book_id: int = None, db: Session = Depends(get_db)):
    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    if book_id is None:
        user_id = 2
        books = get_books_by_user_id(db=db, user_id=user_id)
        db_words = set()
        for book in books:
            book_words = get_user_words_by_book(db=db, book_id=book.book_id)
            for book_word in book_words:
                db_words.add(get_db_word_by_en_word(db=db, en_word=book_word.en_word))
        return db_words

    else:
        book_words = get_user_words_by_book(db=db, book_id=book_id)
        db_words = set()
        for book_word in book_words:
            db_words.add(get_db_word_by_en_word(db=db, en_word=book_word.en_word))
        return db_words

