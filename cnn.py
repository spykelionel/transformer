import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow import keras
from tensorflow.keras import layers

# Load data from CSV
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

# Function to build and train the model
def build_and_train_model(X_train, y_train, num_classes):
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=50, batch_size=16, validation_split=0.2)
    return model

# Build and train the model
num_classes = len(label_encoder.classes_)
model = build_and_train_model(X_train_scaled, y_train, num_classes)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test_scaled, y_test)
print(f'Test accuracy: {test_acc}')

# Save the model
model.save('component_objective_model.h5')

# Load the model
loaded_model = keras.models.load_model('component_objective_model.h5')
# Evaluate the model on the test set
test_loss, test_acc = loaded_model.evaluate(X_test_scaled, y_test)
print(f'Test accuracy: {test_acc*100}')

# Example prediction
sample_input = np.array([[70, 55]])  # Replace with your input
scaled_input = scaler.transform(sample_input)
decoded_prediction = loaded_model.predict_step(scaled_input)
# decoded_prediction = label_encoder.inverse_transform()
print(f'Predicted Component Objectif: {decoded_prediction}')
