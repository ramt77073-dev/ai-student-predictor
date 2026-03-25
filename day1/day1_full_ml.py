import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("==== Loading Data ====")
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print(df.head(), "\n")
print("Data Shape:", df.shape)

print("\n==== Splitting Data ====")
x = df.drop(columns=["species"])
y = df["species"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Training samples: ", len(x_train))
print("Testing samples: ", len(x_test))

print("\n==== Training Model ====")
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

print("Model trained successfully.")

print("\n==== Making Predictions ====")
y_pred = model.predict(x_test)

print("Predicted Values:")
print(list(y_pred), "\n")

print("Actual Values: ")
print(list(y_test.values), "\n")

print("==== Accuracy ====")
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", round(accuracy * 100, 2), "%")

print("\n==== Done ====")