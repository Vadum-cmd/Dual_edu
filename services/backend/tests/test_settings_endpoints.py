from conftest import client

#
def test_settings_get():
    with open("tests/jwt_for_test.txt", "r") as file:
        jwt = file.read()

    response = client.get(url=f"/settings?jwt={jwt}")

    print(response.text)

    assert response.status_code == 200
    # assert response.json() == {}


def test_settings_post():
    with open("tests/jwt_for_test.txt", "r") as file:
        jwt = file.read()

    goal_level = "C2"
    email_adress = "test@gmail.com"  # TODO: remove
    user_level = "B2"
    native_language = "Spanish"
    response = client.post(url=f"/settings?jwt={jwt}&goal_level={goal_level}&email_adress={email_adress}&user_level={user_level}&native_language={native_language}")

    print(response.text)

    assert response.status_code == 200
