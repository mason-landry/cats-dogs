import os
import tensorflow as tf
from matplotlib import pyplot
import sys

from model import PetNet
from load_data import load_data

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
    batch_size = 32
    image_size = (200,200)

    train_ds, val_ds = load_data(train_data, batch_size=batch_size, image_size=image_size)
    model = PetNet.build()

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    H = model.fit(train_ds, epochs=200, verbose=1, validation_data=val_ds)

    # Show curves
    summarize_diagnostics(H)

    # serialize the model to disk
    print("[INFO] serializing digit model...")
    model.save("model.h5")