from fastapi import Depends, APIRouter, Request
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_db_word_by_en_word, change_user_word_status, get_random_user_book, \
    get_unknown_user_word_by_book_id, get_books_by_user_id, get_user_words_by_book, get_user_profile
from logic.get_xlsx import create_xlsx_file
from auth.jwt_decoder import decode_user

router = APIRouter()


@router.get("/vocabulary/download/")  # , ressponse_class=FileResponse
def download_table(request: Request, levels_str: str, db: Session = Depends(get_db)):
    jwt = request.headers['Cookie'].split('=')[1]

    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    books = get_books_by_user_id(db=db, user_id=user_id)
    db_words = set()
    levels = [level.lower() for level in levels_str.split()]

    for book in books:
        book_words = get_user_words_by_book(db=db, book_id=book.book_id)
        for book_word in book_words:
            db_word = get_db_word_by_en_word(db=db, en_word=book_word.en_word)
            if db_word.word_level in levels:
                db_words.add(db_word)

    user_info = get_user_profile(db=db, user_id=user_id)

    path = create_xlsx_file(db_words, user_info.user_name, user_info.native_language)  # TODO: uk_word from db

    return FileResponse(path, filename=path.split("/")[-1], media_type="multipart/form-data")
    # headers = {'Content-Disposition': f'inline; filename="{path}"'}
    #     return FileResponse(path, headers=headers)
