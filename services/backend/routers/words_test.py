from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_user_word, get_word
# from schemas.new_schema import WordUpdate

app = FastAPI()

@app.get("/test")
def get_random_word(user_id: int, db: Session = Depends(get_db)):
    word = get_user_word(db=db, user_id=user_id)
    return {"word_id": word.word_id, "word": word.en_word}

@app.post("/test")
def check_word(word_id: int, answer: str, db: Session = Depends(get_db)):
    if answer.lower() == get_word(db=db, word_id=word_id).uk_word.lower():
        #update_word(db=db, word_id=word_id, word=WordUpdate())
        # TODO: write update_word
        return {"result": True}
    return {"result": False, "correct_answer": get_word(db=db, word_id=word_id).uk_word}

