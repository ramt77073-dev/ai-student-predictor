from fastapi import FastAPI
import pandas as pd
from sklearn.linear_model import LogisticRegression

app = FastAPI()

data = {
    "hours": [1,2,3,4,5,6,7,8],
    "pass": [0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df["pass"]

model = LogisticRegression()
model.fit(X,y)

@app.get("/")
def home():
    return {"message": "ML API working!"}

@app.get("/predict")
def predict(hours: int, marks: int, threshold: float = 0.7):
    new_data = pd.DataFrame([[hours]], columns=["hours"])

    prob = model.predict_proba([hours, marks])[0][1]

    if prob > threshold:
        result = "Pass"
    else:
        result = "Fail"

    return {
        "hours":hours,
        "marks": marks,
        "pass_probability": round(prob, 3),
        "result": result
    }