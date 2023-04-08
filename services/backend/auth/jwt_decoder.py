import jwt
from config.config import SECRET_CODE_JWT, SECRET_CODE_RESET_PASSWORD, AUDIENCE

def decode_user(token: str):
    """
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(jwt=token,
                              key=SECRET_CODE_JWT,
                              audience=[AUDIENCE],
                              algorithms=["HS256"])

    return decoded_data

def decode_user_to_reset_password(token: str):
    """
        :param token: jwt token
        :return:
        """
    decoded_data = jwt.decode(jwt=token,
                              key=SECRET_CODE_RESET_PASSWORD,
                              audience=[AUDIENCE],
                              algorithms=["HS256"])

    return decoded_data

# print(type(decode_user("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1IiwiYXVkIjpbImZhc3RhcGktdXNlcnM6YXV0aCJdLCJleHAiOjE2ODA4ODQ0MjN9.MgRga3FqW8O_YTfdUMnALEuxx8qhpnYITp1iFu2gpUg")['sub']))
