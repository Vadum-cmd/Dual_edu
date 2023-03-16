from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "mysql://sql7603430:HZalYsm789@sql7.freemysqlhosting.net:3306/sql7603430"
SQLALCHEMY_DATABASE_URL = "mysql://root:uTnw0PIh65_!@127.0.0.1:3306/dual_edu"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)