import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import TensorBoard
import skimage as sk
from skimage import data, io, filters, color
#from scipy.misc import *
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os, sys

# Get images
X = []
for filename in os.listdir('Train/'):
    X.append(img_to_array(load_img('Train/'+filename)))
X = np.array(X, dtype=float)


# Set up training and test data
split = int(0.95*len(X))
Xtrain = X[:split]
Xtrain = 1.0/255*Xtrain

#Design the neural network
model = tf.keras.models.Sequential()
tf.keras.layers.InputLayer(input_shape=(256, 256, 1))
tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')
tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', strides=2)
tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same')
tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same', strides=2)
tf.keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same')
tf.keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same', strides=2)
tf.keras.layers.Conv2D(512, (3, 3), activation='relu', padding='same')
tf.keras.layers.Conv2D(256, (3, 3), activation='relu', padding='same')
tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same')
tf.keras.layers.UpSampling2D((2, 2))
tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')
tf.keras.layers.UpSampling2D((2, 2))
tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')
tf.keras.layers.Conv2D(2, (3, 3), activation='tanh', padding='same')
tf.keras.layers.UpSampling2D((2, 2))

# Compile the results of our model
model.compile(optimizer='rmsprop', loss='mse')

# Image transformer
datagen = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.2,
        rotation_range=20,
        horizontal_flip=True)

# Generate training data
batch_size = 50
def image_a_b_gen(batch_size):
    for batch in datagen.flow(Xtrain, batch_size=batch_size):
        lab_batch = color.rgb2lab(batch)
        X_batch = lab_batch[:,:,:,0]
        Y_batch = lab_batch[:,:,:,1:] / 128
        yield (X_batch.reshape(X_batch.shape+(1,)), Y_batch)

# Train model
TensorBoard(log_dir='/output')
model.fit_generator(image_a_b_gen(batch_size), steps_per_epoch=10000, epochs=1)

# Test images
Xtest = sk.color.rgb2lab(1.0/255*X[split:])[:,:,:,0]
Xtest = Xtest.reshape(Xtest.shape+(1,))
Ytest = sk.color.rgb2lab(1.0/255*X[split:])[:,:,:,1:]
Ytest = Ytest / 128
print(model.evaluate(Xtest, Ytest, batch_size=batch_size))

# Load black and white images
color_me = []
for filename in os.listdir('Test/'):
        color_me.append(img_to_array(load_img('Test/'+filename)))
color_me = np.array(color_me, dtype=float)
color_me = sk.color.rgb2lab(1.0/255*color_me)[:,:,:,0]
color_me = color_me.reshape(color_me.shape+(1,))

# Test model
output = model.predict(color_me)
output = output * 128

# Output colorizations
for i in range(len(output)):
        cur = np.zeros((256, 256, 3))
        cur[:,:,0] = color_me[i][:,:,0]
        cur[:,:,1:] = output[i]
        plt.imsave("Results/"+str(i)+".jpg", sk.color.lab2rgb(cur))
