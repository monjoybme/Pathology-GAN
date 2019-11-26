'''https://www.kaggle.com/crawford/resize-and-save-images-as-hdf5-256x256
This code can be used to convert images into ONE h5 file where the Key address will be "train_img" or change it in line 49 '''

import cv2
import datetime as dt
import h5py
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import numpy as np
import os
import pandas as pd
from glob import glob


start = dt.datetime.now()
    # ../input/
PATH = os.path.abspath(os.path.join('/home/msaha6/Downloads/Pathology-GAN/dataset/vgh_nki/', 'he'))
    # ../input/sample/images/
SOURCE_IMAGES = os.path.join(PATH, "patches_h224_w224", "training_data")
    # ../input/sample/images/*.png
images = glob(os.path.join(SOURCE_IMAGES, "*.png"))
images.sort()
     
  
NUM_IMAGES = len(images)
HEIGHT = 224
WIDTH = 224
CHANNELS = 3
SHAPE = (HEIGHT, WIDTH, CHANNELS)
    #Now we will write the h5 file
train_shape = (len(images), HEIGHT, WIDTH, CHANNELS)

hf=h5py.File('data.h5', 'w')
hf.create_dataset("train_img", shape=train_shape, maxshape=train_shape, compression='gzip', compression_opts=9)

for i, img in enumerate(images):
    s=dt.datetime.now()
    img=cv2.imread(images[i])
    img= cv2.resize(img, (WIDTH,HEIGHT), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hf["train_img"][i, ...] = img[None]
    e=dt.datetime.now()
hf.close()
    





