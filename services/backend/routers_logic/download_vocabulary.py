from sqlalchemy.orm import Session
from crud.crud_functions import get_db_word_by_en_word, get_books_by_user_id, get_user_words_by_book, get_user_profile

from logic.get_xlsx import create_xlsx_file


def download_vocabulary(user_id: int, levels_str: str, db: Session):

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

    path = create_xlsx_file(db_words, user_info.email, user_info.native_language)

    return path
