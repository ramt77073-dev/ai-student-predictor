import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = {
    "hours": [1, 2, 3, 4, 5, 6],
    "marks": [40, 50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

X = df[["hours"]]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Parameters:")
print("Slope (m):", model.coef_)
print("Intercept (c):", model.intercept_)

y_pred = model.predict(X_test)

print("\nPredictions:")
for h, actual, pred in zip(X_test.values, y_test.values, y_pred):
    print(f"Hours: {h[0]} | Actual: {actual} | Predicted: {pred}")

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

print("\nEvaluation Metrics:")
print("MAE:", mae)
print("MSE:", mse)
print("R-squared:", r2)

new_hours = pd.DataFrame([[7]], columns=["hours"])
preds = model.predict(new_hours)

print("\nFuture Predictions:")
for h, p in zip(new_hours["hours"], preds):
    print(f"Hours: {h} | Predicted Marks: {p}")

print("\nPrediction for 7 hours study:")
print(f"Predicted Marks: {preds[0]}")
