import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

X = np.array([
    [4, 40],
    [5, 45],
    [6, 50],
    [7, 55],
    [8, 60],
    [9, 65],
    [6, 65],
    [7, 70],
    [8, 75],
    [4, 70]
], dtype=float)

y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1], dtype=int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("X test:\n", X_test)
print("Y test:", y_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_prob = model.predict_proba(X_test_scaled)[:, 1]
print("\nPass probabilities:", y_prob)

thresholds = [0.5, 0.6, 0.7, 0.8, 0.9]

for t in thresholds:
    print("\n" + "=" * 40)
    print(f"Threshold = {t}")

    y_pred = (y_prob >= t).astype(int)

    cm = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print("Confusion Matrix [ [TN FP], [FN TP]]:")
    print(cm)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

new_student = np.array([[6, 60]])
new_student_scaled = scaler.transform(new_student)

prob = model.predict_proba(new_student_scaled)[0][1]
threshold = 0.7
prediction = int(prob >= threshold)

print("\nNew Student:", new_student)
print("Pass probability:", round(prob, 3))
print(f"Using threshold {threshold} -> Predicted:",
      "Pass (1)" if prediction == 1 else "Fail (0)")

