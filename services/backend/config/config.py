from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")


SECRET_CODE_JWT = os.environ.get("SECRET_CODE_JWT")
SECRET_CODE_RESET_PASSWORD = os.environ.get("SECRET_CODE_RESET_PASSWORD")
AUDIENCE = os.environ.get("AUDIENCE")
