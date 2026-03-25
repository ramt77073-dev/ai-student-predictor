import numpy as np
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [40, 45, 50, 55, 60, 65, 70, 75]
}

df = pd.DataFrame(data)
df["pass"] = (df["marks"] >= 50).astype(int)

X = df[["hours", "marks"]]
y = df["pass"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

threshold = 0.6

class Student(BaseModel):
    hours: float
    marks: float

@app.post("/predict")
def predict(student: Student):
    new_student = pd.DataFrame([[student.hours, student.marks]], columns=["hours", "marks"])
    new_student_scaled = scaler.transform(new_student)
    pass_prob = model.predict_proba(new_student_scaled)[0][1]
    return {
        "hours": student.hours,
        "marks": student.marks,
        "pass_probability": round(pass_prob, 3),
        "result": "Pass" if pass_prob >= threshold else "Fail"
    }
