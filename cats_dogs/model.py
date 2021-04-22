# import the necessary packages
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout


class PetNet:
    @staticmethod
    def build():
        # initialize the model
        model = Sequential()
        inputShape = (100,100,3)

        # # softmax classifier
        # model.add(Dense(classes))
        # model.add(Activation("softmax"))
        

        model.add(Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=inputShape))
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.2))
        model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.2))
        model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.2))
        model.add(Flatten())
        model.add(Dense(256, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(1, activation='sigmoid'))

        # model = Sequential()
        # model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=inputShape))
        # model.add(MaxPooling2D((2, 2)))
        # model.add(Dropout(0.2))
        # model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
        # model.add(MaxPooling2D((2, 2)))
        # model.add(Dropout(0.2))
        # model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
        # model.add(MaxPooling2D((2, 2)))
        # model.add(Dropout(0.2))
        # model.add(Flatten())
        # model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        # model.add(Dropout(0.5))
        # model.add(Dense(1, activation='sigmoid'))
        return model