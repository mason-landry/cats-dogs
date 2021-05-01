from glob import glob   # Needed to get folder and file names
from pathlib import Path    # Needed to create and verify sorting folders
import os   # Needed to move images to sorted folder (rename function)

## Set main directory. I have a folder called 'data', which contains both 'test' and 'train' folders. we want the 'train' folder
train_dir = 'data\\train\\'

Path(train_dir).mkdir(parents=True, exist_ok=True)    

## We want a 'cat' and 'dog' folder in the 'data/train' folder
cat_train_dir = train_dir + 'cat\\'
dog_train_dir = train_dir + 'dog\\'

Path(cat_train_dir).mkdir(parents=True, exist_ok=True)    # Create 'cat' folder if it doesn't exist

## Fetch a list of image paths from our 'train' folder
images = glob(train_dir + '*.jpg')

## Loop to check whether 'cat' or 'dog' is in each filename, and move the image accordingly
for i, v  in enumerate(images):
    name = str(v).split('\\')[2] # Get the filename only (without the leading path directories)
    print(i, name)

    if 'cat' in  name:
        os.rename(v, cat_train_dir + name)    # "Move" the file by renaming its path
    
    elif 'dog' in  name:
        os.rename(v, dog_train_dir + name)    # "Move" the file by renaming its path