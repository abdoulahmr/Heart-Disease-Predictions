import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
import numpy as np

# Load your data
df = pd.read_csv("/datasets/data0.csv")

# sample data for prediction
sample_data = np.array([[37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0]])

# Split features and target
X = df.drop("heart_disease", axis=1)
y = df["heart_disease"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost
model = XGBClassifier(eval_metric='logloss')
model.fit(X_train, y_train)

# Prediction on test set
predictions = model.predict(X_test)

# Prediction for sample data
sample_prediction = model.predict(sample_data)
proba = model.predict_proba(sample_data)
risk_percentage = proba[0][1] * 100

print("✅ Disease Detected" if sample_prediction[0] == 1 else "❌ No Heart Disease")
print(f"Risk of heart disease: {risk_percentage:.2f}%")
