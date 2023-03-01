import shutil

from fastapi import FastAPI, Depends, UploadFile, File
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
async def post_book(file: UploadFile = File(...), level: str = "A1", db: Session = Depends(get_db)):
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file.filename)
    words = get_unique_words(text)
    print(words)

    # content = await file.read()
    # split text from book
    # write words to DB using level
    # return words to user
    return {"file_name": file.filename, "words": words}

