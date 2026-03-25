import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

hours = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
marks = np.array([60, 65, 70, 75, 80, 85, 90])

model = LinearRegression()
model.fit(hours, marks)

predicted_marks = model.predict(hours)
plt.scatter(hours, marks, color="blue", label="Actual Data")

plt.plot(hours, predicted_marks, color="red", label="ML Prediction Line")

plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Linear Regression: Hours vs Marks")
plt.show()