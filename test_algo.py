import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np

#f = open("COLPIXVALS.txt", "w")
img = Image.open("01dZiW.jpg")
#image = img_to_array(load_img('01dZiW.jpg'))
img = np.array(img, dtype=float)

#print(img)

# Set up training and test data
split = int(0.80*len(img))
Xtrain = img[:split]
Xtrain = 1.0/255*Xtrain

# We now begin designing our neural network
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Finish model
model.compile(optimizer='rmsprop', loss='mse')
print(model)