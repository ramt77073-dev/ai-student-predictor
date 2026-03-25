import matplotlib
matplotlib.use("TkAgg")
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "marks": [50, 60, 70, 80, 90, 95, 100, 85, 75, 65],
    "result": [0, 0, 0, 1, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["hours", "marks"]].values
y = df["result"].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)

x_min, x_max = X_scaled[:,0].min()-1, X_scaled[:,0].max()+1
y_min, y_max = X_scaled[:,1].min()-1, X_scaled[:,1].max()+1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))
grid = np.c_[xx.ravel(), yy.ravel()]

probs = model.predict_proba(grid)[:,1].reshape(xx.shape)

plt.figure(figsize=(7,5))
plt.contourf(xx, yy, probs, levels=20, cmap="RdBu", alpha=0.6)
plt.scatter(X_scaled[y==0,0], X_scaled[y==0,1], c="blue", label="Fail (0)")
plt.scatter(X_scaled[y==1, 0], X_scaled[y==1, 1], c="red", label="Pass (1)")
plt.colorbar(label="Pass Probability")
plt.legend()
plt.title("Decision Boundary (Logistic Regression)")
plt.xlabel("Hours (scaled)")
plt.ylabel("Marks (scaled)")
plt.savefig('decision_boundary.png', dpi=300, bbox_inches='tight')
print("Plot saved as 'decision_boundary.png'")
plt.show()