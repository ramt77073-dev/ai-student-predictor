import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "marks": [30, 35, 40, 50, 55, 60, 65, 70, 80, 90],
    "result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["hours", "marks"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n==== Evaluation =====")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

new_student = pd.DataFrame([[4, 60]], columns=["hours", "marks"])
new_student_scaled = scaler.transform(new_student)

prob = model.predict_proba(new_student_scaled)
print("\n===== New Student =====")
print("Fail Probability:", prob[0][0])
print("Pass Probability:", prob[0][1])

if prob[0][1] >= 0.5:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
