import smtplib
import ssl
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas

from auth.db import User, get_user_db
from config.config import SECRET_CODE_RESET_PASSWORD, EMAIL_ADDRESS, EMAIL_PASSWORD, FRONTEND_URL


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_CODE_RESET_PASSWORD
    verification_token_secret = SECRET_CODE_RESET_PASSWORD

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        #user_dict["experience"] = 0  # TODO:
        user_dict["experience"] = 0
        user_dict["frame_path"] = "../avatars/avatar1.png"

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = EMAIL_ADDRESS
        receiver_email = user.email
        password = EMAIL_PASSWORD
        message = f"""Subject: Reset password\n\n {FRONTEND_URL}/resetpassword?token={token}"""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message, )

        print(f"User {user.id} has forgot their password. Reset token: {token}")


    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = EMAIL_ADDRESS
        receiver_email = user.email
        password = EMAIL_PASSWORD
        message = f"""Subject: Verify email\n\n {FRONTEND_URL}/verification?token={token}"""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)