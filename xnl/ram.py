import numpy as np

X = np.array([
    [1, 40],
    [2, 42],
    [3, 45],
    [4, 50],
    [5, 55],
    [6, 60],
    [7, 65],
    [8, 70],
    [9, 75],
    [10, 80],
])

y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

new_student = np.array([[6, 68]])

prob = model.predict_proba(new_student)[0][1]
print("Pass Probability:", prob)
print("Fail Probability:", 1 - prob)

if prob > 0.5:
    print("The student is predicted to pass.")
else:
    print("The student is predicted to fail.")
