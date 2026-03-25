import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

X = np.array([
    [2, 30],
    [3, 45],
    [4, 40], 
    [5, 50],
    [6, 55],
    [7, 60],
    [8, 70],
    [7, 55],
    [6, 60],
    [5, 40],
    [4, 30],
    [3, 25],
    [2, 50]
], dtype=float)

y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

probs = model.predict_proba(X_test_scaled)[:, 1]

threshold = 0.6
y_pred =  (probs >= threshold).astype(int)

cm = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("Confusion Matrix:")
print(cm)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)