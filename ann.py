import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow import keras
from tensorflow.keras import layers


print("Starting..")
# Function to generate random data
def generate_data(num_samples=100):
    np.random.seed(42)
    labels = ["C1", "C2", "C3", "C4", "C5", "C6"]
    data = {'Cost': np.random.randint(1, 100, size=num_samples),
            'Duration': np.random.randint(1, 100, size=num_samples),
            'Component_Step_Objectif': np.random.choice(labels, size=num_samples)}
    df = pd.DataFrame(data)
    return df

# Function to preprocess data
def preprocess_data(data):
    label_encoder = LabelEncoder()
    data['Component_Step_Objectif'] = label_encoder.fit_transform(data['Component_Step_Objectif'])
    X = data[['Cost', 'Duration']]
    y = data['Component_Step_Objectif']
    return X, y, label_encoder

# Function to build and train the model
def build_and_train_model(X_train, y_train, num_classes):
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
    return model

# Function to make predictions
def make_predictions(model, X_test, label_encoder):
    predictions = model.predict(X_test)
    decoded_predictions = label_encoder.inverse_transform(np.argmax(predictions, axis=1))
    return decoded_predictions

# Generate data
num_samples = 1000
df = generate_data(num_samples)

# Preprocess data
X, y, label_encoder = preprocess_data(df)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the input data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

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

# Example prediction
sample_input = np.array([[70, 55]])  # Replace with your input
scaled_input = scaler.transform(sample_input)
decoded_prediction = make_predictions(loaded_model, scaled_input, label_encoder)
print(f'Predicted Component Step Objectif: {decoded_prediction}')
