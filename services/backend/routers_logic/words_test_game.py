from sqlalchemy.orm import Session
from crud.crud_functions import get_db_word_by_en_word, change_user_word_status, get_random_user_book, \
    get_unknown_user_word_by_book_id


def get_random_word(user_id: int, db: Session):

    book = get_random_user_book(db=db, user_id=user_id)
    word = get_unknown_user_word_by_book_id(db=db, book_id=book.book_id)

    return {"word": word, "book_id": book.book_id} #.en_word


def check_user_answer(en_word: str, answer: str, book_id: int, db: Session):
    if answer.lower() == get_db_word_by_en_word(db=db, en_word=en_word).uk_word.lower():
        change_user_word_status(db=db, book_id=book_id, en_word=en_word)
        return {"result": True}
    else:
        return {"result": False, "correct_answer": get_db_word_by_en_word(db=db, en_word=en_word).uk_word}