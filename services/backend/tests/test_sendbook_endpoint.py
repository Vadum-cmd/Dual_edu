from conftest import client


def test_sendbook():
    response = client.post('/login', data={
        "grant_type": "",
        "username": "test@gmail.com",
        "password": "test",
        "scope": "",
        "client_id": "",
        "client_secret": "",
    })
    jwt = response.cookies["user_auth"]

    cookies = {
        'user_auth': jwt
    }

    headers = {
        'Accept-Language': 'en-US,en;q=0.9,uk-UA;q=0.8,uk;q=0.7,ru;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryPlBcf3f9ATosJwJB',
        # 'Cookie': 'user_auth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODE5MjAyOTh9.hNP2nUy3-BwwP0aFxovqng8-IGjW3GcxJUY3mzb7Yfs',
        'Origin': 'http://192.168.0.163:8081',
        'Referer': 'http://192.168.0.163:8081/docs',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'accept': 'application/json',
    }

    params = {
        'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODE5MjAyOTh9.hNP2nUy3-BwwP0aFxovqng8-IGjW3GcxJUY3mzb7Yfs',
        'level': 'b1',
    }

    filename = "test_books/test2.pdf"
    data = '------WebKitFormBoundaryPlBcf3f9ATosJwJB\r\nContent-Disposition: form-data; name="file"; filename="' + filename + '"\r\nContent-Type: application/pdf\r\n\r\n\r\n------WebKitFormBoundaryPlBcf3f9ATosJwJB--\r\n'

    # response = requests.post(
    #     'http://192.168.0.163:8081/sendbook',
    #     params=params,
    #     cookies=cookies,
    #     headers=headers,
    #     data=data,
    #     verify=False,
    # )
    print(data)
    # with open('tests/test_books/test2.pdf', 'rb') as f:
    #     file = f.read()
    response = client.post(url=f"/sendbook",
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                           )

    assert response.status_code == 200
    # assert response.json() == {}