from fastapi.responses import FileResponse
from main import app


@app.get("/download-vocabulary", response_class=FileResponse)
async def main():
    return #some_file_path