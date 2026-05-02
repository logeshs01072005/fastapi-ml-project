import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset
data = {
    "age": [25, 30, 45, 35],
    "salary": [30000, 50000, 70000, 60000],
    "experience": [1, 3, 10, 5],
    "target": [0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["age", "salary", "experience"]]
y = df["target"]

model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl created successfully")