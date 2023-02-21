from fastapi import FastAPI


app = FastAPI()

@app.get("/vocabulary")
def get_vocabulary():
    dictionary = {}
    for i in range(1500):
        dictionary[f"word_{i}"] = f"translation_{i}"
    return {"frame type": "avatats/654__frame_type_2.png", "level": 97, "unknown words": dictionary}
