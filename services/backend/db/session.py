from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import DB_HOST, DB_PORT, DB_PASS, DB_USER, DB_NAME

#SQLALCHEMY_DATABASE_URL = "mysql://sql7603430:HZalYsm789@sql7.freemysqlhosting.net:3306/sql7603430"
#SQLALCHEMY_DATABASE_URL = "mysql://root:uTnw0PIh65_!@127.0.0.1:3306/dual_edu"
SQLALCHEMY_DATABASE_URL = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
