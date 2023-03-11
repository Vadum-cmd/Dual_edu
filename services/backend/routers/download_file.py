from typing import List

from fastapi import Depends, APIRouter
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from dependencies import get_db
from crud.crud_functions import get_db_word_by_en_word, change_user_word_status, get_random_user_book, \
    get_unknown_user_word_by_book_id

router = APIRouter()

@router.get("/vocabulary/download/", response_class=FileResponse)
def download_table(user_id: int, levels: List[str], db: Session = Depends(get_db)):
    return None