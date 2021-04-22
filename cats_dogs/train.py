import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
from tensorflow.keras.optimizers import SGD, RMSprop
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from matplotlib import pyplot
import sys

from model import PetNet

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

## plot diagnostic learning curves
def summarize_diagnostics(history):
    fig = pyplot.figure(figsize=(12,8))
    # plot loss
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    pyplot.ylim([0,5])

    ax1.set_title('Cross Entropy Loss')
    ax1.plot(history.history['loss'], color='blue', label='train')
    ax1.plot(history.history['val_loss'], color='orange', label='test')
    ax1.set_ylim([0,5])
    # plot accuracy
    ax2.set_title('Classification Accuracy')
    ax2.plot(history.history['accuracy'], color='blue', label='train')
    ax2.plot(history.history['val_accuracy'], color='orange', label='test')
    ax2.set_ylim([0,1])
    
    # save plot to file
    filename = sys.argv[0].split('/')[-1]
    pyplot.savefig(filename + '_plot.png')
    pyplot.close()

if __name__ == "__main__":
    ## Define train and test paths
    train_data = '.\\data\\train'
    val_data = '.\\data\\val'

    batch_size = 64
    image_size = (100,100)
    train_imagedatagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    validation_imagedatagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    train_ds = train_imagedatagenerator.flow_from_directory(
        train_data,
        target_size=image_size,
        batch_size=64,
        class_mode='binary')

    val_ds = validation_imagedatagenerator.flow_from_directory(
        val_data,
        target_size=image_size,
        batch_size=64,
        class_mode='binary')


    model = PetNet.build()
    opt = SGD(lr=0.001, momentum=0.9)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # H = model.fit(train_ds, steps_per_epoch=100, validation_steps=100, epochs=20, verbose=1, validation_data=val_ds)
    H = model.fit(train_ds, epochs=200, verbose=1, validation_data=val_ds)

    # Show curves
    summarize_diagnostics(H)

    # serialize the model to disk
    print("[INFO] serializing digit model...")
    model.save("model.h5")