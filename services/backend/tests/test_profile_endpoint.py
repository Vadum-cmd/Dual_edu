from conftest import client


def test_profile_get():
    response = client.post('/login', data={
        "grant_type": "",
        "username": "test@gmail.com",
        "password": "test",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    })
    jwt = response.cookies["user_auth"]

    response = client.get(url=f"/profile?jwt={jwt}")
    #print(response.text)
    assert response.status_code == 200
    # assert response.json() == {}