from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_book, get_user_words, DBWord, UserWord
from crud.crud_functions import get_user_words_by_book, get_book_by_user_id, get_db_word_by_en_word
# from schemas.new_schema import UserWord, DBWord


router = APIRouter()


@router.get("/vocabulary")
def get_vocabulary(user_id: int, db: Session = Depends(get_db)):
    #user_vocabulary = get_user_words(db=db, user_id=user_id)
    books = get_book_by_user_id(db=db, user_id=user_id)
    arr = []
    for book in books:
        arr.append(get_user_words_by_book(db=db, book_id=book.book_id))
    print(arr)
    # TODO: arr -> DBWord-s
    return arr

@router.get("/vocabulary/{book_id}")
def get_vocabulary(book_id: int, db: Session = Depends(get_db)):
    user_words = get_user_words_by_book(db=db, book_id=book_id)
    # if book_id == 4:
    #
    #     return {"words": arr}
    db_words = set()
    for user_word in user_words:
        db_words.add(get_db_word_by_en_word(db=db, en_word=user_word.en_word))
    #return {"words": words}
    return db_words
