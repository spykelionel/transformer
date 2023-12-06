import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load the data
data = pd.read_csv('transformer.csv')

# Preprocess data
label_encoder = LabelEncoder()
data['Component_Step_Objectif'] = label_encoder.fit_transform(data['Component_Step_Objectif'])
X = data[['Cost', 'Duration']]
y = data['Component_Step_Objectif']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the input data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the Random Forest model
model_rf = RandomForestClassifier(n_estimators=100, random_state=42)
model_rf.fit(X_train_scaled, y_train)

# Evaluate the model on the test set
test_acc_rf = model_rf.score(X_test_scaled, y_test)
print(f'Test accuracy (Random Forest): {test_acc_rf}')

# Save the model if needed
# from joblib import dump
# dump(model_rf, 'random_forest_model.joblib')
