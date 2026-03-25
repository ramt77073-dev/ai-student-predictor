import pandas as pd

print("===== PANDAS DAY 1 =====")


df = pd.read_csv("setosa_clean.csv")

print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Last 5 rows ---")
print(df.tail())

print("\n--- Shape of data ---")
print(df.shape)  

print("\n--- Column names ---")
print(df.columns)

print("\n--- Basic statistics ---")
print(df.describe())

print("\n--- Checking missing values ---")
print(df.isnull().sum())

print("\n--- Selecting one column (sepal_length) ---")
print(df["sepal_length"].head())

print("\n--- Selecting multiple columns ---")
print(df[["sepal_length", "sepal_width"]].head())

print("\n--- Filtering: all rows where sepal_length > 5.0 ---")
print(df[df["sepal_length"] > 5.0].head())

print("\n--- Filtering: class = setosa ---")
print(df[df["species"] == "setosa"].head())

print("\n--- Sorting by sepal_length (descending) ---")
print(df.sort_values("sepal_length", ascending=False).head())

print("\n--- Group by class (mean values) ---")
print(df.groupby("species").mean())

print("\n===== PANDAS DAY 1 COMPLETED =====")
