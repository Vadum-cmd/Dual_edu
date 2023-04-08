import jwt


def decode_user(token: str):
    """
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(jwt=token,
                              key='SECRET',
                              audience=["fastapi-users:auth"],
                              algorithms=["HS256"])

    return decoded_data

# print(type(decode_user("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1IiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODA4ODQ0MjN9.MgRga3FqW8O_YTfdUMnALEuxx8qhpnYITp1iFu2gpUg")['sub']))
