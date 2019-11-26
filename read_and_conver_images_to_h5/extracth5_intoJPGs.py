import h5py
import matplotlib.pyplot as plt
import imageio
from PIL import Image
import numpy as np
#import pdb
import os
import pandas as pd
import pdb
hdf = h5py.File('data.h5', 'r')
print("Keys: %s" % hdf.keys())


path= '/home/msaha6/Downloads/Pathology-GAN/dataset/vgh_nki/he/patches_h224_w224/training_data/'
extracted_image_path = '/home/msaha6/Downloads/Pathology-GAN/dataset/vgh_nki/he/patches_h224_w224/'
a_group_key = list(hdf.keys())[0]
#a_group_key1 = list(hdf.keys())[0]
data = list(hdf[a_group_key])
#print(data)
#print(a_group_key)
#print(a_group_key1)


array = hdf["train_img"][:]
for image in range(len(array)):
    #pdb.set_trace()
    img=Image.fromarray(array[image].astype('uint8'), 'RGB')
    fullpath = os.path.join(extracted_image_path,'%s.png' % image)
    img.save(fullpath)
    
    #img.show()
    



#array = hdf["train_labels"][:]
#pd.DataFrame(array).to_csv("train_labels.csv")
