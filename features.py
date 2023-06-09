import os
import numpy
import keras
from features_extractor import get_feature

# Calculating features for the dataset
directory = 'path to dataset' # Dataset contains a folder for each class: 'chameleon','juliana','kenzo','rema'
artists = ['chameleon','juliana','kenzo','rema']

features = []
labels = []

for artist in artists:
  print("Calculating features for artist : " + artist)
  for file in os.listdir(directory+"/"+artist):
    file_path = directory+"/"+artist+"/"+file
    features.append(get_feature(file_path))
    label = artists.index(artist)
    labels.append(label)

# Splitting the dataset into training, validation and testing set
permutations = numpy.random.permutation(1049)
features = numpy.array(features)[permutations]
labels = numpy.array(labels)[permutations]

features_train = features[0:843]
labels_train = labels[0:843]

features_val = features[843:948]
labels_val = labels[843:948]

features_test = features[948:1049]
labels_test = labels[948:1049]

# Model Architecture Development
# Input layer
inputs = keras.Input(shape=(498,1), name="feature")

# First Convolutional Layer
x = keras.layers.Conv1D(filters=32, kernel_size=5, activation='relu')(inputs)
x = keras.layers.MaxPooling1D(pool_size=2)(x)

# Second Convolutional Layer
x = keras.layers.Conv1D(filters=64, kernel_size=5, activation='relu')(x)
x = keras.layers.MaxPooling1D(pool_size=2)(x)

# Flatten Layer
x = keras.layers.Flatten()(x)

# Dense Layer
x = keras.layers.Dense(units=128, activation='relu')(x)

# Dropout Layer
x = keras.layers.Dropout(0.5)(x)

# Output Dense Layer
outputs = keras.layers.Dense(units=4, activation='softmax')(x)

# CNN Model
model = keras.Model(inputs=inputs, outputs=outputs)

# Compile Model
model.compile(
    # Optimizer
    optimizer=keras.optimizers.RMSprop(),
    # Loss function to minimize
    loss=keras.losses.SparseCategoricalCrossentropy(),
    # List of metrics to monitor
    metrics=[keras.metrics.SparseCategoricalAccuracy()]
)

# Fit data to model for training
model.fit(
    x=features_train.tolist(),
    y=labels_train.tolist(),
    verbose=1,validation_data=(features_val.tolist(),
    labels_val.tolist()),
    epochs=100
 )

# Save Model
model.save('artist_classifier.h5')
