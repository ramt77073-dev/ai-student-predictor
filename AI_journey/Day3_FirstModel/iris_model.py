import numpy as np
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print("HEAD:\n", df.head(), "\n")
print("Shape:", df.shape)  


from sklearn.model_selection import train_test_split


X = df.drop(columns=['species'])
y = df['species']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


acc = accuracy_score(y_test, y_pred)
print("\n✅ Model trained successfully!")
print("Accuracy:", round(acc * 100, 2), "%")

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
print("Model trained successfully!")

y_pred = model.predict(X_test)
print("Predictions:", y_pred)
print("Actual:", y_test.values)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


