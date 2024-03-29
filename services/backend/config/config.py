from dotenv import load_dotenv
import os

load_dotenv()

FRONTEND_URL = os.environ.get("FRONTEND_URL")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
DB_USER_TEST = os.environ.get("DB_USER_TEST")
DB_PASS_TEST = os.environ.get("DB_PASS_TEST")

SECRET_CODE_JWT = os.environ.get("SECRET_CODE_JWT")
SECRET_CODE_RESET_PASSWORD = os.environ.get("SECRET_CODE_RESET_PASSWORD")
AUDIENCE = os.environ.get("AUDIENCE")
