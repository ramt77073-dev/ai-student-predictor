import pandas as pd

data = {
    "hours": [1, 2, 3, 4, 5, 6],
    "marks": [35, 45, 55, 65, 75, 85],
    "result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

X = df[["hours", "marks"]]
y = df["result"]
from sklearn.model_selection import train_test_split
X_train, X_test,  y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Predictions:", y_pred.values if hasattr(y_pred, "values") else y_pred)
print("Actual    :", y_test.values)

from sklearn.metrics import accuracy_score
accuarcy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuarcy)

new_student = pd.DataFrame([[7, 80]], columns=["hours", "marks"])
result = model.predict(new_student)
if result[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")

proba = model.predict_proba(X_test)
print("\nPrediction Probabilities:")
for h, p in zip(X_test.values, proba):
    print(f"Hours: {h[0]}, Marks: {h[1]} -> Fail: {p[0]:.2f}, Pass: {p[1]:.2f}")
