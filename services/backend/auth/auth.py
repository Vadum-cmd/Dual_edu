from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from config.config import SECRET_CODE_JWT

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name="user_auth", cookie_secure=False, cookie_httponly=False)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_CODE_JWT, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
