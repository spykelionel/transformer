import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten, GlobalMaxPool1D, Dropout, Attention
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from keras.losses import sparse_categorical_crossentropy
from keras.optimizers import Adam
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Your data
data = [[24, 52, ['C4',]], 
        [15, 93, []],
        [32, 15, ['C5','C3']], 
        [44, 72, ['C1','C2','C4']], 
        [24, 61, ['C6','C2',]],
        [25, 21, []],
        [65, 83, ['C5']],
        [67, 87, ['C4']],
        [28, 75, ['C4', 'C5']],
        [92, 75, ['C6','C1']], 
        [53, 88, ['C2','C4',]],
        [42, 24, ['C2','C4','C6']], 
        [34, 3, ['C4','C2']],
        [30, 22, ['C6']],
        [23, 53, ['C6','C4']],
        [43, 2, []],
        [93, 88, ['C5','C2']],
        [17, 30, []],
        [23, 38, ['C4','C5']],
        [43, 2, []]]

# Convert data to DataFrame
df = pd.DataFrame(data, columns=['Cost', 'Duration', 'Component_Step_Objectif'])
try:
    df.drop('id')
except:
    print("Could not drop clm")

# Preprocess your data
# ...

# Tokenizing the Text
maxlen = 5  # Adjust this based on the number of unique components
max_words = 10  # Adjust based on your vocabulary size
tokenizer = Tokenizer(num_words=max_words, lower=True)
tokenizer.fit_on_texts(df['Component_Step_Objectif'].apply(lambda x: ' '.join(x)))

def get_features(text_series):
    sequences = tokenizer.texts_to_sequences(text_series)
    return pad_sequences(sequences, maxlen=maxlen)

x = df[['Cost', 'Duration']].values
y_component = df['Component_Step_Objectif'].values

# Encode the categorical target variable
label_encoder = LabelEncoder()
y_component_encoded = label_encoder.fit_transform(y_component)

# Splitting Data
x_train, x_test, y_component_train, y_component_test = train_test_split(
    x, y_component_encoded, test_size=0.2, random_state=42)

# Building a Model for Component Prediction
component_model = Sequential()
component_model.add(Dense(64, activation='relu', input_shape=(2,)))
component_model.add(Dropout(0.1))
component_model.add(Dense(32, activation='relu'))
component_model.add(Dense(len(label_encoder.classes_), activation='softmax'))  # Softmax for multi-class classification

component_model.compile(optimizer='adam', loss=sparse_categorical_crossentropy, metrics=['accuracy'])
component_model.summary()

# Training the Component Model
callbacks = [
    ReduceLROnPlateau(),
    EarlyStopping(patience=4),
    ModelCheckpoint(filepath='model_component.h5', save_best_only=True)
]

history_component = component_model.fit(x_train, y_component_train,
                                        epochs=20,
                                        batch_size=32,
                                        validation_split=0.1,
                                        callbacks=callbacks)

# Evaluate the Component Model
component_model = keras.models.load_model('model_component.h5')
metrics_component = component_model.evaluate(x_test, y_component_test)
print("Component Model - Loss: {}, Accuracy: {}".format(metrics_component[0], metrics_component[1]))
