import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

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

# Function to apply data augmentation
def apply_data_augmentation(X_train, y_train):
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    augmented_data = []
    augmented_labels = []
    
    for X_batch, y_batch in datagen.flow(X_train.values, y_train.values, batch_size=len(X_train)):
        augmented_data.extend(X_batch)
        augmented_labels.extend(y_batch)
        break
    
    return np.array(augmented_data), np.array(augmented_labels)

# Function to build and train the model
def build_and_train_model(X_train, y_train, num_classes):
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dense(128, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.2)
    return model

# Function to make predictions
def make_predictions(model, X_test, label_encoder):
    predictions = model.predict(X_test)
    decoded_predictions = label_encoder.inverse_transform(np.argmax(predictions, axis=1))
    return decoded_predictions

# Generate data
num_samples = 1000
df = generate_data(num_samples)

print(df.head())

# Preprocess data
X, y, label_encoder = preprocess_data(df)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply data augmentation
X_train_augmented, y_train_augmented = apply_data_augmentation(X_train, y_train)

# Standardize the input data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_augmented)
X_test_scaled = scaler.transform(X_test)

# Build and train the model
num_classes = len(label_encoder.classes_)
model = build_and_train_model(X_train_scaled, y_train_augmented, num_classes)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test_scaled, y_test)
print(f'Test accuracy: {test_acc}')

# Save the model
model.save('component_objective_model.h5')

# Load the model
loaded_model = keras.models.load_model('component_objective_model.h5')
# Evaluate the model on the test set
test_loss, test_acc = loaded_model.evaluate(X_test_scaled, y_test)
print(f'Test accuracy: {test_acc}')

# Example prediction
sample_input = np.array([[70, 55]])  # Replace with your input
scaled_input = scaler.transform(sample_input)
decoded_prediction = make_predictions(loaded_model, scaled_input, label_encoder)
print(f'Predicted Component Step Objectif: {decoded_prediction}')
