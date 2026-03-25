import numpy as np

X = np.array([
    [1, 35], [2, 40], [3, 45], [4, 50], [5, 55],
    [6, 60], [7, 65], [8, 70], [9, 75], [10, 80],
    [4, 65], [5, 58], [6, 52], [7, 68], [8, 62],
    [3, 55], [2, 48], [9, 78], [10, 72], [1, 42]
])

y = np.array([
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    1, 0, 0, 1, 0,
    0, 0, 1, 1, 0
])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

y_pred = model.predict(X_test_scaled)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))