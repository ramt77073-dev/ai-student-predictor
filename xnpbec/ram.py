import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "pass": [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["hours"]]
y = df["pass"]

model = LogisticRegression()
model.fit(X, y)

new_student = pd.DataFrame([[3]], columns=["hours"])
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

threshold = 0.7
pass_prob = probability[0][1]
if pass_prob >= threshold:
    result = "pass"
else:
    result = "Fail"

for threshold in [0.4, 0.5, 0.6, 0.7]:
    result = "pass" if pass_prob >= threshold else "Fail"
    print(f"Threshold {threshold} -> {result}")

print("Prediction (0=Fail, 1=Pass):", prediction[0])
print("Probability:", probability)