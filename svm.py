import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load data from 'transformer.csv'
df = pd.read_csv('transformer.csv')

# Preprocess data
label_encoder = LabelEncoder()
df['Component_Step_Objectif'] = label_encoder.fit_transform(df['Component_Step_Objectif'])
X = df[['Cost', 'Duration']]
y = df['Component_Step_Objectif']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the input data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create an SVM classifier
svm_classifier = SVC(kernel='linear', C=1.0, random_state=42)

# Train the SVM model
svm_classifier.fit(X_train_scaled, y_train)

# Make predictions on the test set
svm_predictions = svm_classifier.predict(X_test_scaled)

# Calculate the accuracy
svm_accuracy = accuracy_score(y_test, svm_predictions)
print(f'Test accuracy (SVM): {svm_accuracy}')
