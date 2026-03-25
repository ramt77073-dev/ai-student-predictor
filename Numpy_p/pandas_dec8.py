import pandas as pd
data = {
    "name": ["Ram", "teja", "Sai"],
    "age": [22, 24, 28],
    "marks": [90, 85, 75]
}
df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df["name"])
print(df[["name", "age", "marks"]])
print(df.iloc[0])
print(df.iloc[1:3])
print(df[df["marks"] > 80])

df["status"] = ["Pass", "Pass", "Fail"]
print(df)

df = df.drop("status", axis=1)
print(df)

df2 = pd.DataFrame({
    "name": ["A", "B", None],
    "age": [20, None, 22]
})
print(df2.isnull().sum())
print(df2.fillna("Unknown"))
print(df2.dropna())