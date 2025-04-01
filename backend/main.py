from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "AI 飲食助理運作中 🚀"}