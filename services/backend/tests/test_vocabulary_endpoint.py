import json
from conftest import client
from crud.crud_functions import get_books_by_user_id, get_user_words_by_book


def test_get_vocabulary(mocker):
    with open("tests/jwt_for_test.txt", "r") as file:
        jwt = file.read()
    id = 1
    get_books_by_user_id_mock = mocker.patch("get_books_by_user_id")
    get_books_by_user_id_mock.return_value = {}

    get_user_words_by_book_mock = mocker.patch("get_user_words_by_book")
    get_user_words_by_book_mock.return_value = {}


def test_vocabulary_endpoint():
    with open("tests/jwt_for_test.txt", "r") as file:
        jwt = file.read()

    book_id = 13

    response = client.get(url=f"/vocabulary?jwt={jwt}&book_id={book_id}")

    vocabulary = json.loads(response.text)

    print("TODO: check vocabulary somehow")
    assert type(vocabulary) == list