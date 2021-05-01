from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from pathlib import Path
from glob import glob
import cv2
import os

test_dir = 'data\\fussel_test\\'
cat_dir = test_dir + 'cat_predictions\\'
dog_dir = test_dir + 'dog_predictions\\'

Path(cat_dir).mkdir(parents=True, exist_ok=True)    # Create 'cat_predictions' folder if it doesn't exist
Path(dog_dir).mkdir(parents=True, exist_ok=True)    # Create 'dog_predictions' folder if it doesn't exist

model = load_model('model.h5')
images = glob(test_dir + '*.jpg')

for idx, image in enumerate(images):

    img = cv2.imread(image)
    img = cv2.resize(img, (200,200))
    img = img.astype("float32") / 255.0
    img = img_to_array(img)
    img = img.reshape(1, 200, 200, 3)

    # Prediction
    pred = model.predict(img)[0][0]
    print(pred)
    
    if pred < 0.5:
        name = cat_dir + 'cat_' + str(pred) + '.jpg'
        os.rename(image, name)    # "Move" the file by renaming its path
    else:
        name = dog_dir + 'dog_' + str(pred) + '.jpg'
        os.rename(image, name)    # "Move" the file by renaming its path
        
