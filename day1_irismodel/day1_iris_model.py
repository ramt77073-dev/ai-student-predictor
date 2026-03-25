from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

print("===== IRIS FLOWER ML MODEL ====\n")

data = load_iris()

x = data.data
y = data.target

print("Features names: ", data.feature_names)
print("Target names:", data.target_names, "\n")

print("First 5 rows of x(features:)")
print(x[:5])
print("First 5 rows of y(target:)")
print(y[:5])
print("\nTotal samples:", x.shape[0])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("\nTraining samples:", x_train.shape[0])
print("Testing samples:", x_test.shape[0])

model = DecisionTreeClassifier(random_state=42)

model.fit(x_train, y_train)
print("\nModel training complete")

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("\n==== Model Evalution ====")
print("Accuracy:", round(accuracy * 100, 2), "%\n")

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

print("\n===== PREDICTION ON NEW SAMPLE ======")
new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])

pred_class_index = model.predict(new_flower)[0]
pred_class_name = data.target_names[pred_class_index]

print("New flower measurements:", new_flower[0])
print("Predicted class index:", pred_class_index)
print("Predicted class name:", pred_class_name)

print("\n====== END OF DAY 1 ML MODEL =====")

