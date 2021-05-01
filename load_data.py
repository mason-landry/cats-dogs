import tensorflow as tf

def load_data(train_data, batch_size=32, image_size=(50,50)):

    ## Define the data generator
    train_gen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        validation_split=0.25, # Take 25% of the data to use for validation
        horizontal_flip=True,
        fill_mode='nearest')

    train_ds = train_gen.flow_from_directory(
        train_data,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='binary',
        subset='training')  # Point to 75% of data reserved for training

    val_ds = train_gen.flow_from_directory(
        train_data,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='binary',
        subset='validation') # Point to 25% of data reserved for validation
    
    return train_ds, val_ds