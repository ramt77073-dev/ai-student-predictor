from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
result = np.array([0,0,0,0,1,1,1,1,1,1])

X_train, X_test, y_train, y_test = train_test_split(hours, result, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Test data:", X_test.flatten())
print("Predictions:", predictions)
print("Actual:", y_test)