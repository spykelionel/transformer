import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding, Flatten, GlobalMaxPool1D, Dropout, Conv1D
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from sklearn.preprocessing import StandardScaler

# Load the data from CSV
df = pd.read_csv('random_data.csv')

# Flatten the 'Component_Objectif' lists
df['Component_Objectif'] = df['Component_Objectif'].apply(eval)

# Extracting features and labels
features = df[['Cost', 'Duration']].values
labels = df['Component_Objectif']

# Convert labels to a multi-label binary format
mlb = MultiLabelBinarizer()
labels = mlb.fit_transform(labels)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Build the CNN model
model = Sequential()
model.add(Dense(512, input_dim=2, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(len(mlb.classes_), activation='sigmoid'))  # Output layer

model.history

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Define callbacks
callbacks = [
    ReduceLROnPlateau(),
    EarlyStopping(patience=4),
    ModelCheckpoint(filepath='model-cnn.keras', save_best_only=True)
]

# Train the model
history = model.fit(x_train, y_train, epochs=20, batch_size=128, validation_split=0.1, callbacks=callbacks)

# Evaluate the model on the test set
metrics = model.evaluate(x_test, y_test)
print("Loss: {}".format(metrics[0]))
print("Accuracy: {}".format(metrics[1]))
