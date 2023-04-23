import json
from conftest import client


def test_vocabulary_endpoint():
    with open("tests/jwt_for_test.txt", "r") as file:
        jwt = file.read()

    book_id = 13

    response = client.get(url=f"/vocabulary?jwt={jwt}&book_id={book_id}")

    vocabulary = json.loads(response.text)

    print("TODO: check vocabulary somehow")
    assert type(vocabulary) == list