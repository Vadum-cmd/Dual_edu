import shutil

from fastapi import Depends, UploadFile, File, APIRouter
from sqlalchemy.orm import Session


from auth.jwt_decoder import decode_user
from dependencies import get_db
from logic.extract_words_and_translate import extract_text_from_pdf, word_tokenization
from crud.crud_functions import BookCreate, create_book, get_db_word_by_en_word, UserWordCreate, create_user_word, \
    get_books_by_user_id, get_user_words_by_book
from logic.get_xlsx import create_xlsx_file

router = APIRouter()

@router.post("/sendbook")
def post_book(jwt: str, level: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    books = get_books_by_user_id(db=db, user_id=user_id)
    for book in books:
        book_words = get_user_words_by_book(db=db, book_id=book.book_id)
        identifier = False
        for word in book_words:
            if not (word in book_words):
                identifier = True
                break
        if identifier == False:
            return {"book_id": book.book_id}

    path = f'books/{file.filename}'

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    book = BookCreate(**{"user_id": user_id, "book_title": file.filename, "book_author": ""})
    db_book = create_book(db=db, book=book)

    text = extract_text_from_pdf(path)
    words = word_tokenization(text)

    for word in words:
        try:
            db_word = get_db_word_by_en_word(db=db, en_word=word)

            if db_word.word_level > level:
                user_word = UserWordCreate(**{"en_word": db_word.en_word, "book_id": db_book.book_id, "is_known": False})
                create_user_word(db=db, user_word=user_word)
        except:
            pass  # print(word)

    return {"book_id": db_book.book_id}


