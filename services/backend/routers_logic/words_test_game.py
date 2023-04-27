from sqlalchemy.orm import Session
from crud.crud_functions import get_db_word_by_en_word, change_user_word_status, get_random_user_book, \
    get_unknown_user_word_by_book_id, get_user_profile, add_exp, get_user_id_by_book_id
from schemas.schema import WordForVocabulary


def get_random_word(user_id: int, db: Session):

    book = get_random_user_book(db=db, user_id=user_id)
    word = get_unknown_user_word_by_book_id(db=db, book_id=book.book_id)

    user_language = get_user_profile(user_id=user_id, db=db).native_language
    if user_language == "Ukrainian":
        translation = word.uk_word
    else:
        translation = word.es_word
    new_word = WordForVocabulary(**{"word": word.en_word, "translation": translation, "word_level": word.word_level})

    return {"word": new_word, "book_id": book.book_id} #.en_word


def check_user_answer(en_word: str, answer: str, book_id: int, db: Session):
    if answer.lower() == get_db_word_by_en_word(db=db, en_word=en_word).uk_word.lower():
        level = get_db_word_by_en_word(db=db, en_word=en_word).word_level
        change_user_word_status(db=db, book_id=book_id, en_word=en_word)
        user_id = get_user_id_by_book_id(db=db, book_id=book_id)
        print(user_id)
        if level == "a2":
            exp = 25
        elif level == "b1":
            exp = 30
        elif level == "b2":
            exp = 35
        elif level == "c1":
            exp = 40
        elif level == "c2":
            exp = 45
        else:
            exp = 20
        add_exp(db=db, user_id=user_id, exp=exp)

        return {"result": True}
    else:
        return {"result": False, "correct_answer": get_db_word_by_en_word(db=db, en_word=en_word).uk_word}
