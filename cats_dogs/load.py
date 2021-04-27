from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from pathlib import Path
from glob import glob
import cv2
import os

test_dir = 'data\\test\\test1\\'
cat_val_dir = test_dir + 'cat\\'
dog_val_dir = test_dir + 'dog\\'
unsure_dir = test_dir + 'unsure\\'

Path(cat_val_dir).mkdir(parents=True, exist_ok=True)    # Create 'cat' folder if it doesn't exist
Path(dog_val_dir).mkdir(parents=True, exist_ok=True)    # Create 'dog' folder if it doesn't exist
Path(unsure_dir).mkdir(parents=True, exist_ok=True)    # Create 'unsure' folder if it doesn't exist

model = load_model('model.h5')
# model.summary()

for image in glob(unsure_dir + '*.jpg'):
    name = str(image).split('\\')[3] # Get the filename only (without the leading path directories)

    img = cv2.imread(image)
    img = cv2.resize(img, (200,200))
    cv2.imshow("unsure",img)
    cv2.waitKey(0)
    # img = img.astype("float32") / 255.0
    # img = img_to_array(img)
    # img = img.reshape(1, 200, 200, 3)

    # # Prediction
    # pred = model.predict(img)
    
    # if pred < 0.3:
    #     os.rename(image, cat_val_dir + name)    # "Move" the file by renaming its path
    # elif pred > 0.7:
    #     os.rename(image, dog_val_dir + name)    # "Move" the file by renaming its path
    # else:
    #     os.rename(image, unsure_dir + name)    # "Move" the file by renaming its path
        
