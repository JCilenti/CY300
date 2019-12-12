# First import the necessary dependencies
'''
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from numpy import asarray
from os import listdir
from matplotlib import image
'''
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from PIL import Image
import numpy as np
import os, sys

# Import images from Train directory
X = []
for filename in os.listdir('Train/'):
    X.append(img_to_array(load_img('Train/' + filename)))
X = np.array(X, dtype = float)

# Prepare image data for training/testing
split = int(0.80 * len(X))
X_Train = X[:split]
X_Train = 1.0/255 * X_Train # Make all image values 0 - 1

# Designing the neural network
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])


