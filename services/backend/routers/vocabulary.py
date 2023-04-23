from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from dependencies import get_db
from routers_logic.get_vocabulary import get_vocabulary

router = APIRouter()


@router.get("/vocabulary")
def get_vocabulary_endpoint(jwt: str, book_id: int = None, db: Session = Depends(get_db)):
    try:
        user_id = int(decode_user(jwt)['sub'])
    except:
        return None

    return get_vocabulary(user_id=user_id, book_id=book_id, db=db)

