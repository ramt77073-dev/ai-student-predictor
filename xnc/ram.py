import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix

data = {
    "hours": [1, 2, 3, 4, 5, 6],
    "marks": [35, 45, 55, 65, 75, 85],
    "result": [0, 0, 0, 1, 1, 1]
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

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred, labels=[0, 1]))

new_student = pd.DataFrame([[4, 60]], columns=["hours", "marks"])
new_student = scaler.transform(new_student)

prediction = model.predict(new_student)
prob = model.predict_proba(new_student)

print("\nNew Student Predictions:")
print("Fail Probability:", prob[0][0])
print("Pass Probability:", prob[0][1])
print("Result:", "Pass" if prediction[0] == 1 else "Fail")