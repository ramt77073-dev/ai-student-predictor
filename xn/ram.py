import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

Data = {
    "hours": [1, 2, 3, 4, 5, 6],
    "marks": [35, 45, 55, 65, 75, 85],
    "result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(Data)
X = df[["hours", "marks"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

new_student = pd.DataFrame([[4, 60]], columns=["hours", "marks"])
result = model.predict(new_student)

if result[0] == 1:
    print("The student will pass.")
else:
    print("The student will not pass.")
