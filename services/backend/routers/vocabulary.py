from fastapi import FastAPI


app = FastAPI()

@app.get("/vocabulary")
def get_vocabulary():
    dict = {}
    for i in range(1500):
        dict[f"word_{i}"] = f"translation_{i}"

    return {"frame type": "avatars/1__frame_type_2.png", "level": 97, "unknown words": dict}