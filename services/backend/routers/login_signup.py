# from fastapi import FastAPI, status, HTTPException, Depends
# from fastapi.security import OAuth2PasswordRequestForm
# from schemas import UserOut, UserAuth, TokenSchema #!?
# from passlib.context import CryptContext
# import os
# from datetime import datetime, timedelta
# from typing import Union, Any
# from jose import jwt
#
# from fastapi.responses import RedirectResponse
# from sqlalchemy.orm import Session
# from dependencies import get_db
# from uuid import uuid4
#
#
# ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
# REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
# ALGORITHM = "HS256"
# JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']  # should be kept secret
# JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']  # should be kept secret
#
# password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
#
# def get_hashed_password(password: str) -> str:
#     return password_context.hash(password)
#
#
# def verify_password(password: str, hashed_pass: str) -> bool:
#     return password_context.verify(password, hashed_pass)
#
#
# def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#
#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
#     return encoded_jwt
#
#
# def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
#
#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
#     return encoded_jwt
#
#
#
#
#
# @app.post('/signup', summary="Create new user", response_model=UserOut)
# async def create_user(data: UserAuth):
#     # querying database to check if user already exist
#     user = db.get(data.email, None)
#     if user is not None:
#             raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User with this email already exist"
#         )
#     user = {
#         'email': data.email,
#         'password': get_hashed_password(data.password),
#         'name': data.name
#         'id': str(uuid4())
#     }
#     db[data.email] = user    # saving user to database
#     return user
#
#
# @app.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = db.get(form_data.email, None)
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect email or password"
#         )
#
#     hashed_pass = user['password']
#     if not verify_password(form_data.password, hashed_pass):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect email or password"
#         )
#
#     return {
#         "access_token": create_access_token(user['email']),
#         "refresh_token": create_refresh_token(user['email']),
#     }
