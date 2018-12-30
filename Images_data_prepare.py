import numpy as np
import cv2
import os
import pickle
from tqdm import tqdm
from random import shuffle

data_dir = str(input("Please Input your Data_path: "))
CATEGORIES = os.listdir(data_dir)

size = int(input("please Input your image size that you want to resize: "))

name = str(input("please Input your output file name"))

data = []

def creating_training_data():
    for category in (CATEGORIES):
        path = os.path.join(data_dir, category)
        class_num = CATEGORIES.index(category)
        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_COLOR)
                img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
                new_array = cv2.resize(img_array, (size, size))
                data.append([new_array, class_num])
            except Exception as e:
                pass

shuffle_d = str(input("Do you want to shuffle data? [Y/N]"))
if shuffle_d == 'Y':
    shuffle(data)
if shuffle_d == 'N':
    pass
if shuffle_d =='y':
    shuffle(data)
if shuffle_d == 'n':
    pass

with open(name, 'wb') as f:
    pickle.dump(data, f)
