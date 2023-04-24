from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import Session

from auth.jwt_decoder import decode_user
from crud.crud_functions import get_books_by_user_id
from dependencies import get_db
from routers_logic.get_vocabulary import get_vocabulary


from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


router = APIRouter()


@router.get("/books")
def get_books_endpoint(request: Request, db: Session = Depends(get_db)):
    try:
        jwt = request.headers['Cookie'].split('=')[1]
        user_id = int(decode_user(jwt)['sub'])
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
        #return None

    return get_books_by_user_id(user_id=user_id, db=db)