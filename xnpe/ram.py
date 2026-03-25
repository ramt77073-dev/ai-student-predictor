import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

X = np.array([
    [2, 30],
    [3, 45],
    [4, 40],
    [5, 45],
    [6, 50],
    [7, 55],
    [8, 60],
    [9, 65],
    [6, 65],
    [7, 70],
    [8, 75], 
    [6, 50],
    [7, 55],
    [4, 70]
], dtype=float)

y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1], dtype=int)

def evaluate(y_true, y_pred, title=""):
    cm = confusion_matrix(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    print("\n" + "=" * 55)
    print(title)
    print("Confusion Matrix [ [TN, FP], [FN, TP]] :" )
    print(cm)
    print("Precision:", round(precision, 3))
    print("Recall:", round(recall, 3))
    print("F1 Score:", round(f1, 3))

def train_logistic_and_test(X_features, y, threshold=0.6, label=""):

    X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.3, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_scaled, y_train)

    probs = model.predict_proba(X_test_scaled)[:, 1]

    y_pred = (probs >= threshold).astype(int)

    print("\n" + "-" * 55)
    print(label)
    print("threshold:", threshold)
    print("Test probabilites:", np.round(probs, 3))

    evaluate(y_test, y_pred, title=label)

    return model, scaler

X_before = X.copy()

train_logistic_and_test(
    X_before, y,
    threshold=0.6, 
    label="BEFORE Feature Engineering (hours, marks)"
)
