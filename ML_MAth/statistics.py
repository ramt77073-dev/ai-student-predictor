import numpy as np
data = np.array([70, 75, 80, 85, 90])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("Std Dev:", np.std(data))

import pandas as pd
df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 6],
    "marks": [40, 50, 60, 70, 80, 90]
})
print(df.corr())

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df)
print(scaled)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled = scaler.fit_transform(df)
print(scaled)

from sklearn.preprocessing import LabelEncoder
le =  LabelEncoder()
cities = ["Mumbai", "Delhi", "Chennai"]
print(le.fit_transform(cities))
df = pd.DataFrame({"City": ["Delhi", "Mumbai", "Chennai"]})
print(pd.get_dummies(df))
