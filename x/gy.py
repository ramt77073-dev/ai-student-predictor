import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "hours" : [1, 2, 3, 4, 5, 6],
    "marks" : [35, 45, 55, 65, 75, 85],
    "result" : [0, 0, 0, 1, 1, 1]
}

df =  pd.DataFrame(data)
X = df[["hours", "marks"]]
y = df["result"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accacury:", accuracy_score(y_test, pred))
new_student = pd.DataFrame([[4, 60]], columns=["hours", "marks"])
print("Prediction:", model.predict(new_student))