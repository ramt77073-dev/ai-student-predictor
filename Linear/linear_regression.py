import pandas as pd
data = {
    "hours": [1, 2, 3, 4, 5, 6],
    "marks": [40, 50, 60, 70, 80, 90]
}
df = pd.DataFrame(data)
print(df)
X = df[["hours"]]
y = df["marks"]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
print("Slope (m):", model.coef_)
print("Intercept (b):", model.intercept_)
pred = model.predict(pd.DataFrame([[7]], columns=["hours"]))
print("Predicted marks for 7 hours:", pred)
score = model.score(X, y)
print("Model accuracy:", score)