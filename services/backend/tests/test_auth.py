from conftest import client


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
