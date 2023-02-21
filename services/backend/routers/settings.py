from fastapi import FastAPI


app = FastAPI()

@app.get("/settings")
def get_settings():
    return {}

@app.post("/settings")
def post_settings():
    return {}
