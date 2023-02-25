from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud import get_user, get_user_level

app = FastAPI()

@app.get("/profile")
def get_profile_info(user_id: int, db: Session = Depends(get_db)):
    return get_user(db=db, user_id=user_id)

