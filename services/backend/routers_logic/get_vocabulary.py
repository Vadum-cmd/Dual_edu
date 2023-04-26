from crud.crud_functions import get_books_by_user_id, get_user_words_by_book, get_db_word_by_en_word
from sqlalchemy.orm import Session

from routers_logic.get_word_scheme_from_Db_word_scheme import get_word_from_db_word


def get_vocabulary(user_id: int, book_id: int, db: Session):
    if book_id is None:
        books = get_books_by_user_id(db=db, user_id=user_id)
        db_words = set()

        for book in books:
            book_words = get_user_words_by_book(db=db, book_id=book.book_id)
            for book_word in book_words:
                db_words.add(get_db_word_by_en_word(db=db, en_word=book_word.en_word))

        words_for_vocabulary = []

        for word in db_words:
            words_for_vocabulary.append(get_word_from_db_word(word=word, user_id=user_id, db=db))
        return words_for_vocabulary

    else:
        book_words = get_user_words_by_book(db=db, book_id=book_id)
        db_words = set()
        for book_word in book_words:
            db_words.add(get_db_word_by_en_word(db=db, en_word=book_word.en_word))

        words_for_vocabulary = []

        for word in db_words:
            words_for_vocabulary.append(get_word_from_db_word(word=word, user_id=user_id, db=db))
        return words_for_vocabulary