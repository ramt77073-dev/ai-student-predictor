import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = {
    "hours": [1, 2, None, 4, 5, 6],
    "marks": [80, 85, None, 90, 95, 100],
    "city" : ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)
print("\nMissing Values Count:")
print(df.isnull().sum())

df["hours"].fillna(df["hours"].mean(), inplace=True)
df["marks"].fillna(df["marks"].mean(), inplace=True)

print("\nAfter Filling Missing Values:")
print(df)

df_encoded = pd.get_dummies(df, columns=["city"])
print("\nAfter One-Hot Encoding:")
print(df_encoded)

minmax = MinMaxScaler()
noermalized = minmax.fit_transform(df_encoded)

df_normalized = pd.DataFrame(
    noermalized, columns=df_encoded.columns
)
print("\nNormalized Data (0 to 1):")
print(df_normalized)

standard = StandardScaler()
standardized = standard.fit_transform(df_encoded)

df_standardized = pd.DataFrame(
    standardized, columns=df_encoded.columns
)

print("\nStandardized Preprocessed Dtaset (Standardized):")
print(df_standardized)