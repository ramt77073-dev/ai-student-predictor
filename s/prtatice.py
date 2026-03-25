import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data = {
    "hours": [1, 2, None, 4, 5, 6],
    "marks": [35, None, 55, 65, 75, 85],
    "city": ["mumbai", "delhi", "bangalore", "chennai", "hyderabad", "pune"]
}

df = pd.DataFrame(data)
print("Original Data")
print(df)

print("\nMissing Value:")
print(df.isnull().sum())

df["hours"].fillna(df["hours"].mean(), inplace=True)
df["marks"].fillna(df["marks"].mean(), inplace=True)

print("\nAfter filling missing values")
print(df)

df_encoded = pd.get_dummies(df, columns=["city"])
print("\nAfter Encoding")
print(df_encoded)

scaler = StandardScaler()
scaled = scaler.fit_transform(df_encoded)

df_scaled = pd.DataFrame(scaled,columns=df_encoded.columns)
print("\nFinal Scaled Data")
print(df_scaled)
