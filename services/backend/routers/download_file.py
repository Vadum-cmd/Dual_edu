from typing import List

from fastapi import Depends, APIRouter
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_db_word_by_en_word, change_user_word_status, get_random_user_book, \
    get_unknown_user_word_by_book_id, get_books_by_user_id, get_user_words_by_book
from logic.get_xlsx import create_xlsx_file

router = APIRouter()

@router.get("/vocabulary/download/", response_class=FileResponse)
def download_table(user_id: int, levels: List[str], db: Session = Depends(get_db)):  # level: str = "a1"

    books = get_books_by_user_id(db=db, user_id=user_id)
    db_words = set()

    for book in books:
        book_words = get_user_words_by_book(db=db, book_id=book.book_id)
        for book_word in book_words:
            db_word = get_db_word_by_en_word(db=db, en_word=book_word.en_word)
            if db_word.word_level in levels:
                db_words.add(db_word)

    path = create_xlsx_file(db_words)

    headers = {'Content-Disposition': f'inline; filename="{path}"'}
    return FileResponse(path, headers=headers)
