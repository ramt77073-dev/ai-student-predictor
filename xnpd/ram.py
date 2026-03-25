import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

X = np.array([
    [2, 30],
    [3, 35],
    [4, 40],
    [5, 45],
    [6, 50],
    [7, 55],
    [8, 60],
    [9, 65],
    [6, 65],
    [8, 75],
    [6, 50],
    [7, 55],
    [4, 70]
], dtype=float)

y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1], dtype=int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print("\nX_test:")
print(X_test.astype(int))
print("y_test:", y_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_scaled, y_train)

log_probs = log_model.predict_proba(X_test_scaled)[:, 1]

def evaluate_model(name, y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    print("\n" + "=" * 50)
    print(f"{name}")
    print("Confusion Matrix [ [TN FP], [FN TP]]: ")
    print(cm)
    print("Precision:",round(precision, 3))
    print("Recall:", round(recall, 3))
    print("F1 Score:", round(f1, 3))

print("\nLogistic Probabilities:", np.round(log_probs, 3))

thresholds = [0.5, 0.6, 0.7, 0.8]

for t in thresholds:
    log_pred = (log_probs >= t).astype(int)
    evaluate_model(f"Logistic Regression (threshold={t})", y_test, log_pred)

tree_model = DecisionTreeClassifier(random_state=42, max_depth=3)
tree_model.fit(X_train, y_train)

tree_pred = tree_model.predict(X_test)
evaluate_model("Decision Tree (max_depth=3)", y_test, tree_pred)

new_student = np.array([[6, 60]], dtype=float)

new_student_scaled = scaler.transform(new_student)
new_prob = log_model.predict_proba(new_student_scaled)[0, 1]

chosen_threshold = 0.6
log_result = 1 if new_prob >= chosen_threshold else 0

tree_result = int(tree_model.predict(new_student)[0])

print("\n" + "=" * 50)
print("New Student:", new_student.astype(int))
print("Logistic pass probability:", round(new_prob, 3))
print(f"Logistic (threshold={chosen_threshold})->", "Pass" if log_result == 1 else "Fail")
print("Decision Tree ->", "Pass" if tree_result == 1 else "Fail")


