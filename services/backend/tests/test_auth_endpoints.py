from conftest import client
from fastapi import Form

def test_register():
    response = client.post('/register', json={
        "email": "test@gmail.com",
        "password": "test",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "user_name": "Test",
        "native_language": "Ukrainian",
        "goal_level": "C2",
        "user_level": "A1"
    })

    assert response.status_code == 201


def test_login():
    response = client.post('/login', data={
        "grant_type": "",
        "username": "test@gmail.com",
        "password": "test",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    })

    assert response.status_code == 200
