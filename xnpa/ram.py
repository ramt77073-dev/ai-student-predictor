import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

X = np.array([
    [2, 45],
    [3, 50],
    [4, 55],
    [5, 60],
    [6, 65],
    [7, 70],
    [8, 75],
    [6, 50],
    [7, 55],
    [4, 70],
], dtype=float)

y = np.array([0, 0, 0, 0, 1, 1, 1, 0, 0, 1], dtype=int)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

pass_probs = model.predict_proba(X_test_scaled)[:, 1]

print("\nX_test:")
print(X_test.astype(int))
print("y_test:", y_test)
print("pass probabilities:", np.round(pass_probs, 3))

def evaluate_threshold(threshold: float):
    y_pred = (pass_probs > threshold).astype(int)

    cm = confusion_matrix(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print("\n" +  "=" * 40 )
    print(f"Threshold = {threshold}")
    print("Confusion matrix [ [TN FP], [FN TP]]:")
    print(cm)
    print("Precision:", round(prec, 3))
    print("Recall:", round(rec, 3))
    print("F1-score:", round(f1, 3))


for t in [0.5, 0.6, 0.7, 0.8, 0.9]:
    evaluate_threshold(t)

new_student = np.array([[6, 60]], dtype=float)
new_student_scaled = scaler.transform(new_student)
new_pass_prob = model.predict_proba(new_student_scaled)[0, 1]

print("\n" + "=" * 40)
print("New Student:", new_student.astype(int))
print("Pass probability:", round(new_pass_prob, 3))


chosen_threshold = 0.7
final_pred = 1 if new_pass_prob >= chosen_threshold else 0
print(f"Using threshold {chosen_threshold} -> Predicted:", "Pass (1)" if final_pred == 1 else "fail (0)")