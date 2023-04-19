from conftest import client
#
# #
# def test_settings_get():
#     response = client.post('/login', data={
#         "grant_type": "",
#         "username": "test@gmail.com",
#         "password": "test",
#         "scope": "",
#         "client_id": "",
#         "client_secret": "",
#     })
#     jwt = response.cookies["user_auth"]
#
#     response = client.get(url=f"/settings?jwt={jwt}")
#
#     assert response.status_code == 200
#     # assert response.json() == {}
#
#
# def test_settings_post():
#     response = client.post('/login', data={
#         "grant_type": "",
#         "username": "test@gmail.com",
#         "password": "test",
#         "scope": "",
#         "client_id": "",
#         "client_secret": "",
#     })
#     jwt = response.cookies["user_auth"]
#
#     goal_level = "C2"
#     email_adress = "test@gmail.com"  # TODO: remove
#     user_level = "B2"
#     native_language = "Spanish"
#     response = client.post(url=f"/settings?jwt={jwt}&goal_level={goal_level}&email_adress={email_adress}&user_level={user_level}&native_language={native_language}")
#
#     assert response.status_code == 200
