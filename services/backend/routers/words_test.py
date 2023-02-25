from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud import get_word, update_word
from schemas.new_schema import WordUpdate

app = FastAPI()

@app.get("/test")
def get_random_word(user_id: int, db: Session = Depends(get_db)):
    word = get_random_word(db=db, user_id=user_id)
    return {"word_id": word.id, "word": word.word}

@app.post("/test")
def check_word(user_id: int, word_id: int, word: str, db: Session = Depends(get_db)):
    if word.lower() == get_word(db=db, word_id=word_id).lower():
        update_word(db=db, word_id=word_id, word=WordUpdate())  # TODO: WordUpdate is not written yet
        return {"result": True}
    return {"result": False, "correct_answer": get_word(db=db, word_id=word_id).uk_word}

