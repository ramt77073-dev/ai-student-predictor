from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello bro, API working"}

@app.get("/predict")
def predict(hours: int):
    if hours >= 4:
        return {"result": "Pass"}
    else:
        return {"result": "Fail"}