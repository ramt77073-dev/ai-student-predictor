import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix , precision_score, recall_score, f1_score

X =  np.array([
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
    [5, 58],
    [8, 60],
])

y = np.array([0,0,0,1,1,1,1,0,0,1,0,1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

pass_probs = model.predict_proba(X_test)[:, 1]

print("X_test:\n", X_test)
print("y_test:", y_test)
print("Pass Probabilities:", np.round(pass_probs, 3))

threholds = [0.5, 0.7, 0.8, 0.9]

for t in threholds:
    y_pred = (pass_probs >= t).astype(int)

    cm = confusion_matrix(y_test, y_pred, labels=[0,1])
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print("\n" + "-" * 45)
    print(f"Threshold = {t}")
    print("Confusin Matrix [ [TN FP] [FN TP]]: ")
    print(cm)
    print("Precision:", round(precision, 3))
    print("Recall:", round(recall, 3))
    print("F1 Score:", round(f1, 3))