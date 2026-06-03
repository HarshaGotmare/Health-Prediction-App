import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample patient data
data = {
    'glucose': [80, 120, 140, 200, 95, 160],
    'haemoglobin': [13, 12, 10, 9, 14, 8],
    'cholesterol': [180, 220, 250, 300, 170, 280],
    'risk': [
        'Low Risk',
        'Moderate Risk',
        'High Risk',
        'High Risk',
        'Low Risk',
        'High Risk'
    ]
}

# Convert data into table format
df = pd.DataFrame(data)

# Input features
X = df[['glucose', 'haemoglobin', 'cholesterol']]

# Output labels
y = df['risk']

# Create ML model
model = RandomForestClassifier()

# Train model
model.fit(X, y)

# Save trained model
joblib.dump(model, 'model.pkl')

print("Model trained successfully!")