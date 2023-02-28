from fastapi import FastAPI, Depends, UploadFile, File
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_user_prof
from fastapi import FastAPI, UploadFile,  Form


app = FastAPI()

@app.post("/sendbook")
def post_book(file: UploadFile = File(...), level: str = "A1", db: Session = Depends(get_db)):
    content = await file.read()
    # split text from book
    # write words to DB using level
    # return words to user
    return {}

# import io
# import fitz
# import fastapi
# # import PyMuPDF
#
#
# app = FastAPI()

# @app.post("/sendbook")
# async def get_unfamiliar_words(file: UploadFile = File(...), level: str = Form(...)):
#     content = await file.read()
#     # test print(content)
#
#     pdf = fitz.open(stream=io.BytesIO(content))
#     text = ""
#     for page in pdf:
#         text += page.get_text()
#
#     words = text.split()
#     # You can use your own list of words or import it from a file or a database
#     english_levels = {
#         "a1": ["unfamiliar", "words", "for", "level", "a1"],
#         "a2": ["unfamiliar", "words", "for", "level", "a2"],
#         "b1": ["unfamiliar", "words", "for", "level", "b1"],
#         "b2": ["unfamiliar", "words", "for", "level", "b2"],
#         "c1": ["unfamiliar", "words", "for", "level", "c1"],
#         "c2": ["unfamiliar", "words", "for", "level", "c2"],
#     }
#
#     unfamiliar_words = []
#
#     for word in words:
#         for lvl, wrds in english_levels.items():
#             if level.lower() == lvl:
#                 if word.lower() not in wrds and word.isalpha():
#                     unfamiliar_words.append(word.lower())
#
#     return {"unfamiliar_words": list(set(unfamiliar_words))}

