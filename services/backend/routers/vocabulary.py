from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud import get_user, get_user_words

app = FastAPI()

@app.get("/vocabulary")
def get_vocabulary(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db=db, user_id=user_id)
    user_vocabulary = get_user_words(db=db, user_id=user_id)
    return {"user_name": user.user_name, "user_level": user.user_level}  # TODO: add user_vocabulary

