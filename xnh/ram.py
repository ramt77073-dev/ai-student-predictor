import numpy as np
from sklearn.linear_model import LinearRegression

hours = np.array([1, 2, 3, 4, 5, 6, 7])
marks = np.array([60, 65, 70, 75, 80, 85, 90])

model = LinearRegression()
model.fit(hours.reshape(-1, 1), marks)

predicted_marks = model.predict(hours.reshape(-1, 1))
print(predicted_marks)

new_hours = np.array([[8]])
print(model.predict(new_hours))
    