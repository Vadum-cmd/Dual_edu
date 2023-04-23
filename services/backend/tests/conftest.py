from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import DB_HOST_TEST, DB_PORT_TEST, DB_PASS_TEST, DB_USER_TEST, DB_NAME_TEST
from models.model import metadata

from main import app

from fastapi.testclient import TestClient

SQLALCHEMY_DATABASE_URL = f"mysql://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal_test = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

metadata.bind = engine_test

# async def override_get_async_sesion() ->
# ...

client = TestClient(app)
