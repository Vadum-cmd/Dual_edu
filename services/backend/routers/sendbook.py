from fastapi import Depends, UploadFile, File, APIRouter
from sqlalchemy.orm import Session
from dependencies import get_db
from logic.extract_words_and_translate import extract_text_from_pdf, word_tokenization, translate_word
from crud.crud_functions import UserWordCreate, create_user_word, get_db_word
from crud.crud_functions import BookCreate, create_book, get_db_word_by_en_word, UserWordCreate, create_user_word
router = APIRouter()

@router.post("/sendbook")
def post_book(file: UploadFile = File(...), level: str = "a2", db: Session = Depends(get_db)):# -> List[DBWord]:
    # with open(f'{file.filename}', "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)

    book = BookCreate()
    book.user_id = 45
    book.book_title = file.filename
    book.book_author = None
    db_book = create_book(db=db, book=book)
    print(db_book.book_id)

    text = extract_text_from_pdf(file.filename)
    words = word_tokenization(text)

    for word in words:
        db_word = get_db_word_by_en_word(db=db, en_word=word)
        print(word, db_word)
        if db_word.word_level > level:
            user_word = UserWordCreate()
            user_word.en_word = db_word.en_word
            user_word.book_id = db_book.book_id
            user_word.is_known = False
            user_db_word = create_user_word(db=db, user_word=user_word)
            print(user_db_word)

    # for word in words:
    #     create_user_word(db=db, user_word=UserWordCreate(en_word=word, is_known=False, book_id=book_id))
    #
    # # TODO: what about translation
    # for word in words:
    #     user_words.append(get_db_word(db=db, en_word=word))
    #
    # return user_words


    return {"book_id": db_book.book_id}

    # split text from book
    # write words to DB using level
    # return words to user

    # user_words = {}
    # j = 0
    # for word in words:
    #     user_words[word] = f"Error"
    #     j += 1
    #     if j == 50:
    #         break
    #
    # wb = load_workbook(filename='words_table.xlsx', data_only=True)
    # # data_only=False by default
    # # If you want to see data instead of formulas, set data_only=True
    #
    # ws = wb['Аркуш1']  # Or whatever your sheet name is
    # #
    # # translated_text = translator.translate('안녕하세요.')
    # # print(translated_text.text)
    # #
    # # print(translated_text.text)
    # print("OK by now")
    # for us_word in user_words.keys():
    #     for num_row in range(1, ws.max_row):
    #         if ws[f'A{num_row}'].value == us_word:
    #             try:
    #                 user_words[us_word] = translate_word(us_word)
    #             except:
    #                 print(us_word)
    # print(user_words)
    #return {"words": user_words}
