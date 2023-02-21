from fastapi import FastAPI


app = FastAPI()

@app.get("/test")
def get_word():
    return {"word": "elephant"}

@app.post("/test")
def check_word(word: str):
    if word.lower() == "слон":
        return {"result": True, "new word": "cat"}
    return {"result": False, "correct translation": "слон"}

