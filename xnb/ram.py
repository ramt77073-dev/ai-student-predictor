import pandas as pd
 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "hours": [1, 2, 3, 4, 5, 6],
    "marks": [35, 45, 55, 65, 75, 85],
    "result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print("\n===Dataset====", df)


X = df[["hours", "marks"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()    
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

print("\n==== Evaluation on Test Data ====")
print("Accuracy:", acc)
print("Confusion Matrix:\n", cm)

new_student = pd.DataFrame([[4, 60]], columns=["hours", "marks"])

new_student_scaled = scaler.transform(new_student)

result = model.predict(new_student_scaled)[0]
proba = model.predict_proba(new_student_scaled)[0]

print("\n=== New Student ====")
print("Input:", new_student.values)

print("\n==== Prediction =====")
print("Prediction:", result)
print("Fail Probability:", round(proba[0], 2))
print("Pass Probability:", round(proba[1], 2))

if result == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")