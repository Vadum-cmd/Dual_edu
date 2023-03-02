from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_user_vocab
from main import app


@app.get("/vocabulary")
def get_vocabulary(user_id: int, db: Session = Depends(get_db)):
    user_vocabulary = get_user_vocab(db=db, user_id=user_id)
    return user_vocabulary
