import os

from fastapi import Depends, APIRouter, Request, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from dependencies import get_db
from auth.jwt_decoder import decode_user
from routers_logic.download_vocabulary import download_vocabulary

router = APIRouter()


@router.get("/vocabulary/download/")  # , ressponse_class=FileResponse
def download_vocabulary_endpoint(request: Request, levels_str: str, db: Session = Depends(get_db)):
    try:
        jwt = request.headers['Cookie'].split('=')[1]
        user_id = int(decode_user(jwt)['sub'])
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            # headers={"WWW-Authenticate": "Basic"},
        )
        # return None

    path = download_vocabulary(user_id=user_id, levels_str=levels_str, db=db)

    return FileResponse(path, filename=path.split("/")[-1], media_type="multipart/form-data")

    #return FileResponse(path, filename=path.split("/")[-1], media_type="multipart/form-data")
    # headers = {'Content-Disposition': f'inline; filename="{path}"'}
    #     return FileResponse(path, headers=headers)
