from keras.layers import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers import Activation, Dense, Dropout, Flatten, InputLayer
from keras.layers.normalization import BatchNormalization
from keras.models import model_from_json
from keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from skimage.color import rgb2lab, lab2rgb, rgb2gray
from skimage.io import imsave
import numpy as np
import os
import random
import tensorflow as tf

################################################################

# Get images
X = [] # Create a blank array for the image values
for filename in os.listdir('Train/'):
    X.append(img_to_array(load_img('Train/'+filename)))
X = np.array(X, dtype=float)
# Above we turned all of the image data into arrays
# Set up train and test data
split = int(0.80*len(X)) # Train with 80% of the Training Data
Xtrain = X[:split]
Xtrain = 1.0/255*Xtrain

################################################################

# Here we define the type of model we will be using
# We also construct the neural network
model = Sequential() # Use the Keras Sequential Model witn layers
model.add(InputLayer(input_shape=(256, 256, 1))) # Create the input layer and define the shape
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same', strides=2))
model.add(Conv2D(512, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(Conv2D(2, (3, 3), activation='tanh', padding='same'))
model.add(UpSampling2D((2, 2)))
model.compile(optimizer='rmsprop', loss='mse')
# We created 9 COnvoltruonal layers before we began upscaling
# The upscaling process will be explaiend later
# Image transformer
datagen = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.2,
        rotation_range=20,
        horizontal_flip=True)

# Generate training data
batch_size = 10 # Create our batch of images to be shaped for the model
def image_a_b_gen(batch_size):
    for batch in datagen.flow(Xtrain, batch_size=batch_size):
        lab_batch = rgb2lab(batch)
        X_batch = lab_batch[:,:,:,0]
        Y_batch = lab_batch[:,:,:,1:] / 128
        yield (X_batch.reshape(X_batch.shape+(1,)), Y_batch)

# Train model using tensorboard to display output of model
tensorboard = TensorBoard(log_dir="output/first_run")
model.fit_generator(image_a_b_gen(batch_size), callbacks=[tensorboard], epochs=1, steps_per_epoch=10)

################################################################

# Save model to .JSON format
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# Serializing our wights to the HDF5 format
# This is how they will be imported back in when testing
model.save_weights("model.h5")

################################################################

# Test images with our model
Xtest = rgb2lab(1.0/255*X[split:])[:,:,:,0]
# Convert the images to the lAB colorspace before color
Xtest = Xtest.reshape(Xtest.shape+(1,))
Ytest = rgb2lab(1.0/255*X[split:])[:,:,:,1:]
Ytest = Ytest / 128
print(model.evaluate(Xtest, Ytest, batch_size=batch_size))

################################################################

# Create a new list for the colorized RGB images
color_me = []
for filename in os.listdir('Test/'): # Pull images from the Test directory
    color_me.append(img_to_array(load_img('Test/'+filename)))
color_me = np.array(color_me, dtype=float)
color_me = rgb2lab(1.0/255*color_me)[:,:,:,0]
color_me = color_me.reshape(color_me.shape+(1,))

################################################################

# Test model
output = model.predict(color_me)
output = output * 128
# Evaluate the output of our model 

################################################################

# Output colorizations
for i in range(len(output)):
    cur = np.zeros((256, 256, 3))
    cur[:,:,0] = color_me[i][:,:,0]
    cur[:,:,1:] = output[i]
    imsave("Results/img_"+str(i)+".png", lab2rgb(cur))
    # Return the image to RGB color and place in a new dir called Results
    # Save each as a png file
