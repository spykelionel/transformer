import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Conv1D, GlobalMaxPool1D, Dense, Dropout 
from keras.callbacks import ModelCheckpoint
import joblib  # Import joblib for saving and loading the tokenizer

# Load the dataset
data = pd.read_csv('data.csv')

# Convert lists to strings
data['Component_Objectif'] = data['Component_Objectif'].apply(lambda x: '_'.join(x)) 

# Explode into separate rows
data = data.assign(Component_Objectif=data['Component_Objectif'].str.split('_')).explode('Component_Objectif')

# Drop missing values  
data = data.dropna()

# Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['Component_Objectif'])  

# Tokenize strings to sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data['Component_Objectif'])  
X = tokenizer.texts_to_sequences(data['Component_Objectif'])

# Pad sequences
max_len = max(data['Component_Objectif'].apply(len))
X = pad_sequences(X, maxlen=max_len)   

# Save tokenizer and max_len using joblib
tokenizer_info = {
    'tokenizer': tokenizer,
    'max_len': max_len,
    'label_classes': label_encoder.classes_
}
joblib.dump(tokenizer_info, 'tokenizer_info.joblib')


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   

# Build model   
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=20, input_length=max_len))
model.add(Conv1D(filters=50, kernel_size=3, activation='relu', padding="same"))
model.add(GlobalMaxPool1D()) 
model.add(Dense(50, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(len(label_encoder.classes_), activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Save the tokenizer
joblib.dump(tokenizer, 'tokenizer.joblib')

# Save the model checkpoint
checkpoint = ModelCheckpoint('my_model.h5', save_best_only=True)

# Train model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2, callbacks=[checkpoint])

# Evaluate model 
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy*100:.2f}%')
print(f'Loss: {loss*100:.2f}%')
