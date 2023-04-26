import os
import shutil

from fastapi import UploadFile

from crud.crud_functions import get_books_by_user_id, get_user_words_by_book, get_db_word_by_en_word, create_book, \
    create_user_word
from sqlalchemy.orm import Session

from logic.extract_words_and_translate import extract_text_from_pdf, word_tokenization
from schemas.schema import BookCreate, UserWordCreate


def send_book(user_id: int, level: str, file: UploadFile, db: Session):

    filename = file.filename[:47] + "..." if len(file.filename) > 50 else file.filename

    books = get_books_by_user_id(db=db, user_id=user_id)

    for book in books:
        if book.book_title == filename:
            return {"book_id": book.book_id}

    path = f"books/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)



    book = BookCreate(**{"user_id": user_id, "book_title": filename, "book_author": ""})
    db_book = create_book(db=db, book=book)

    text = extract_text_from_pdf(path)
    words = word_tokenization(text)

    os.remove(f"books/{file.filename}")

    for word in words:
        try:
            db_word = get_db_word_by_en_word(db=db, en_word=word)
            if db_word.word_level > level:
                user_word = UserWordCreate(**{"en_word": db_word.en_word, "book_id": db_book.book_id, "is_known": False})
                create_user_word(db=db, user_word=user_word)
        except:
            # print(word)
            pass

    return {"book_id": db_book.book_id}
