from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_user_prof

app = FastAPI()

@app.get("/profile")
def get_profile_info(user_id: int, db: Session = Depends(get_db)):
    return get_user_prof(db=db, user_id=user_id)

