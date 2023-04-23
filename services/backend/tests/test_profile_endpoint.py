from conftest import client
import json


def test_profile_get():
    with open("tests/jwt_for_test.txt", "r") as file:
        jwt = file.read()

    response = client.get(url=f"/profile?jwt={jwt}")

    profile_info = json.loads(response.text)

    # TODO: what about hashed password ???!
    # TODO: what about frames
    assert response.status_code == 200
    assert profile_info["current_num_level"] == 1
    assert profile_info["goal_level"] == "C2"
    assert profile_info["user_level"] == "B2"
    assert profile_info["user_name"] == "Test"
    assert profile_info["email"] == "test@gmail.com"
    assert profile_info["native_language"] == "Spanish"
