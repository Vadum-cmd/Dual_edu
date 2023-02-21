from fastapi import FastAPI


app = FastAPI()

@app.get("/profile")
def get_profile_info():
    return {}
