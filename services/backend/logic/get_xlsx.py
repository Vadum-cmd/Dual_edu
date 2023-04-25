import time
from typing import Set

import openpyxl

from models.model import DB_word


def create_xlsx_file(words: Set[DB_word], filename, native_language):
    book = openpyxl.Workbook()
    sheet = book.active

    sheet[f'A1'] = "word"
    sheet[f'B1'] = "translation"
    sheet[f'C1'] = "level"

    i = 2
    for word in words:
        sheet[f'A{i}'] = word.en_word
        if native_language == "Ukrainian":
            sheet[f'B{i}'] = word.uk_word
        elif native_language == "Spanish":
            sheet[f'B{i}'] = word.es_word
        sheet[f'C{i}'] = word.word_level
        i += 1

    path = f"xlsx_files/{filename}'s_vocabulary.xlsx"
    book.save(path)

    return path
