# cats-dogs

This is my DNN code for a cats vs dogs image classifier.

I used the resulting model to determine if my cat would be identified as a cat. Read about it here:
https://towardsdatascience.com/is-my-cat-really-a-dog-7fa13c921625

Download the data from Kaggle:

Steps to train your own model:

1. Set up file structure properly:

|data
|   --train
|   --test

|cats_dogs
|   --__init__.py
|   --fussel_test.py
|   --load_data.py
|   --model_test.py
|   --model.py
|   --train.py
|   --sort.py

2. Run `sort.py` to sort training data into `cat` and `dog` folders
3. Run `train.py`, or adjust image_size, batch_size, model parameters, etc. first.


