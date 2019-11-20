import h5py
import matplotlib.pyplot as plt
import imageio
from PIL import Image
import numpy as np
import pdb
import os
import pandas as pd
hdf = h5py.File('hdf5_vgh_nki_he_train.h5', 'r')
print("Keys: %s" % hdf.keys())

a_group_key = list(hdf.keys())[1]
a_group_key1 = list(hdf.keys())[0]
data = list(hdf[a_group_key])
#print(data)
#print(a_group_key)
#print(a_group_key1)

#pdb.set_trace()
#array = hdf["test_img"][:]
#for image in range(len(array)):
    #img=Image.fromarray(array[image].astype('uint8'), 'RGB')
    #print(os.path.basename(array[image]))
    #img.save("test.jpg", "JPEG")
    #img.show()

array = hdf["train_labels"][:]
pd.DataFrame(array).to_csv("train_labels.csv")
