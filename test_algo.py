# First import the necessary dependencies
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import os, sys

img = Image.open("01dZiW.jpg") # import our image
img = np.array(img, dtype=float)
# turn the saturation values of our images into an array

# Set up training and test data
split = int(0.80*len(img)) # Use 80% of data to train model
Xtrain = img[:split]
Xtrain = 1.0/255*Xtrain

# We now begin designing our neural network
# every Conv2D is a convolutional layer for our network
# we pool the data, making the image smaller
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Finish model and create a summary
model.compile(optimizer='rmsprop', loss='mse')
model.summary()
model.get_weights()