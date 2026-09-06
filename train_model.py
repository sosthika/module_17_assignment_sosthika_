import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("heart.csv")

# Features
features = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]

X = df[features]
y = df["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Create model directory
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/heart_model.joblib")

print("Model trained successfully!")
print("Model saved to model/heart_model.joblib")
print("Test accuracy:", model.score(X_test, y_test))