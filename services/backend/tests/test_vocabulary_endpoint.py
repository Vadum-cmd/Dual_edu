import json

import crud
from conftest import client
#from crud.crud_functions import get_books_by_user_id, get_user_words_by_book

from dependencies import get_db
from fastapi import Depends, APIRouter

def test_get_vocabulary(mocker):

    print("TODO: redo this")

    get_books_by_user_id_mock = mocker.patch("crud.crud_functions.get_books_by_user_id")
    get_books_by_user_id_mock.return_value = 1

    get_user_words_by_book_mock = mocker.patch("crud.crud_functions.get_user_words_by_book")
    get_user_words_by_book_mock.return_value = 2

    get_db_word_by_en_word_mock = mocker.patch("crud.crud_functions.get_db_word_by_en_word")
    get_db_word_by_en_word_mock.return_value = 3

    assert crud.crud_functions.get_books_by_user_id(user_id=1, db=Depends(get_db)) == 1
    assert crud.crud_functions.get_user_words_by_book(user_id=1, db=Depends(get_db)) == 2
    assert crud.crud_functions.get_db_word_by_en_word(user_id=1, db=Depends(get_db)) == 3


def test_vocabulary_endpoint():
    with open("tests/jwt_for_test.txt", "r") as file:
        jwt = file.read()

    book_id = 13

    response = client.get(url=f"/vocabulary?jwt={jwt}&book_id={book_id}")

    vocabulary = json.loads(response.text)

    print("TODO: check vocabulary somehow")
    assert type(vocabulary) == list