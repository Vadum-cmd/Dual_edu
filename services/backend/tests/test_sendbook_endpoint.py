import json
from conftest import client


def test_sendbook_endpoint():
    with open("tests/jwt_for_test.txt", "r") as file:
        jwt = file.read()

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
        'jwt': cookies['user_auth'],
        'level': 'b1',
    }

    filename = "test_books/test2.pdf"
    data = '------WebKitFormBoundaryPlBcf3f9ATosJwJB\r\nContent-Disposition: form-data; name="file"; filename="' + filename + '"\r\nContent-Type: application/pdf\r\n\r\n\r\n------WebKitFormBoundaryPlBcf3f9ATosJwJB--\r\n'

    response = client.post(url=f"/sendbook",
                    params=params,
                    cookies=cookies,
                    headers=headers,
                    data=data,
                           )

    sendbook_answer = json.loads(response.text)

    #print("BOOK IS NOT ID DB!!! (PROBABLY BECAUSE SOMEBODY ALREADY DOWNLOADED THE SAME BOOK)")

    assert response.status_code == 200
    assert type(sendbook_answer["book_id"]) == int
