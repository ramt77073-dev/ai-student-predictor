from fastapi import FastAPI
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = joblib.load("iris_model.joblib")

@app.get("/")
def home():
    return {"message": "Hello AI Engineer"}
@app.get("/about")
def about():
    return {"message": "I am becoming an AI Engineer"}

@app.post("/predict")
def predict(data: dict):
    features = [
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]
    prediction = model.predict([features])
    flower_names = ["setosa", "versicolor", "virginica"]
    return {
        "prediction_number": int(prediction[0]),
        "prediction_name": flower_names[int(prediction[0])]
    }