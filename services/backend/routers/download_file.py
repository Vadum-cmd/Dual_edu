from fastapi import APIRouter
from fastapi.responses import FileResponse
from main import app


router = APIRouter()

@router.get("/download-vocabulary", response_class=FileResponse)
async def main():
    return #some_file_path