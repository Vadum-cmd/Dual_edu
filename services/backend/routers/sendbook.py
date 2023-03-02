import shutil
from openpyxl import load_workbook
from fastapi import FastAPI, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from dependencies import get_db
from logic.extract_words_and_translate import get_unique_words, extract_text_from_pdf
from googletrans import Translator
from main import app

# TODO: rewrite this function
@app.post("/sendbook")
async def post_book(file: UploadFile = File(...), level: str = "a2"):  #, level: str = Form()  # , db: Session = Depends(get_db)
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file.filename)
    words = get_unique_words(text)

    # split text from book
    # write words to DB using level
    # return words to user

    user_words = {}
    j = 0
    for word in words:
        user_words[word] = f"Error"
        j += 1
        if j == 50:
            break

    wb = load_workbook(filename='words_table.xlsx', data_only=True)
    # data_only=False by default
    # If you want to see data instead of formulas, set data_only=True

    ws = wb['Аркуш1']  # Or whatever your sheet name is
    translator = Translator()
    #
    # translated_text = translator.translate('안녕하세요.')
    # print(translated_text.text)
    #
    # print(translated_text.text)
    print("OK by now")
    for us_word in user_words.keys():
        for num_row in range(1, ws.max_row):
            if ws[f'A{num_row}'].value == us_word:
                try:
                    user_words[us_word] = [translator.translate(us_word, dest="uk").text, ws[f'C{num_row}'].value]
                except:
                    print(us_word)
    print(user_words)
    return {"words": user_words}