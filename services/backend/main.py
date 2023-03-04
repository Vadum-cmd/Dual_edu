import shutil

from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from dependencies import get_db
from logic.extract_words_and_translate import extract_text_from_pdf, word_tokenization, translate_word
from openpyxl import load_workbook

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sendbook")
def post_book(file: UploadFile = File(...), level: str = "a2", db: Session = Depends(get_db)):# -> List[DBWord]:
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file.filename)
    words = word_tokenization(text)
    user_words = []
    book_id = 4
    # for word in words:
    #     create_user_word(db=db, user_word=UserWordCreate(en_word=word, is_known=False, book_id=book_id))
    #
    # # TODO: what about translation
    # for word in words:
    #     user_words.append(get_db_word(db=db, en_word=word))
    #
    # return user_words
    return_words_222(user_words)
    print({"words": "words"})

    return {"words": "words"}


@app.get("/vocabulary")
def return_words_222(words):
    print(f"{words}")
    return words