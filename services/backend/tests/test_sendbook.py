from conftest import client


# def test_sendbook():
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
#     with open('tests/test_books/test2.pdf', 'rb') as f:
#         file = f.read()
#     response = client.post(url=f"/sendbook?jwt={jwt}&level=b1",
#                     data={
#                         "file": file
#                     },
#                     headers={'Content-Type': 'application/pdf'})
#
#     assert response.status_code == 200
#     # assert response.json() == {}