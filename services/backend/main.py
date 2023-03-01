import shutil

from fastapi import FastAPI, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from dependencies import get_db
from logic.extract_words_and_translate import get_unique_words, extract_text_from_pdf
# from crud.crud_functions import get_user_prof
# from pdfminer.pdfparser import extract_pages, extract_text
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfparser import PDFParser

app = FastAPI()


@app.post("/sendbook")
async def post_book(file: UploadFile = File(...), selectedLevel: str = Form()):#, level: str = Form()  # , db: Session = Depends(get_db)
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file.filename)
    words = get_unique_words(text)
    print(words)

    # split text from book
    # write words to DB using level
    # return words to user

    #print(level)
    #print(level)
    print(file.filename)
    print(selectedLevel)
    return {"file_name": file.filename, "words": words[:100]} # , "words": words
