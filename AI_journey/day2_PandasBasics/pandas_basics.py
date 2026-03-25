import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print("HEAD:\n", df.head(), "\n")
print("INFO:", df.info())
print("DESCRIBE:\n", df.describe())

print("\nOnly sepal_Length column:\n", df["sepal_length"].head())
print("\nFirst 3 rows (iloc):\n", df.iloc[:3])

setosa = df[df['species'] == 'setosa']
print("\nSetosa count: ", len(setosa))

print("\nMissing per column:\n", df.isnull().sum())

df['petal_area'] =df['petal_length'] * df['petal_width']
print("\nNew column added (petal_area):\n", df[['petal_length', 'petal_width', 'petal_area']].head())

top= df.sort_values('petal_area', ascending=False).head(5)
print("\nTop 5 by petal_area\n", top[['species', 'petal_area']])

setosa[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']].to_csv('setosa_clean.csv', index=False)
print("\nsetosa_clean.csv created")