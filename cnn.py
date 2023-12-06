import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
import tensorflow as tf


# Creating a DataFrame with the provided data
data = {
    'Cost': [60, 70, 70, 80, 70, 80, 80, 90, 70, 80, 80, 90, 80, 90, 90],
    'Duration': [60, 55, 55, 50, 55, 50, 50, 45, 55, 50, 50, 45, 50, 45, 45],
    'Component_Step_Objectif': [[], ['C5'], ['C3'], ['C3', 'C4'], ['C2'], ['C2', 'C4'], ['C2', 'C3'], 
                                ['C2', 'C6', 'C4'], ['C1'], ['C1', 'C4'], ['C1', 'C3'], ['C1', 'C3', 'C4'], 
                                ['C1', 'C2'], ['C5', 'C2', 'C6'], ['C1', 'C2', 'C3']]
}

df = pd.DataFrame(data)

# Step 1: Data Preprocessing
X = df[['Cost', 'Duration']]
y = df['Component_Step_Objectif']

mlb = MultiLabelBinarizer()
y_encoded = mlb.fit_transform(y)

# Step 2: Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Step 3: Neural Network Architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(len(mlb.classes_), activation='softmax')  # Output layer with softmax for multi-class classification
])

print("Classes:", len(mlb.classes_))

# Step 4: Model Compilation
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# training
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Step 6: Model Evaluation
# test_loss, test_acc = model.evaluate(X_test, y_test)

# Prediction. Change this data for your own case. 
new_data = pd.DataFrame({'Cost': [50], 'Duration': [92]})
prediction = model.predict(new_data)
decoded_prediction = mlb.inverse_transform((prediction > 0.1).astype(int))
print(f'Predicted Component_Step_Objectif: {decoded_prediction}')
