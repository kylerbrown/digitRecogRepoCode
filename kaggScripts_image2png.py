import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pylab as plt
import os

# load data
train = pd.read_csv('../data/train.csv')

def makeImageArray(train,indx,plots = 0):
    label = train.iloc[indx,0]
    arr = np.array(train.iloc[indx,1:], dtype=np.uint8)
    arr.resize((28, 28))
    if plots:
        plt.figure()
        plt.imshow(arr)



# now draw all the numbers
# NOTE: This is just a sample that runs to
# completion on the Kaggle site.
# To get the PNGs for the full dataset,
# uncomment everything from line 24 to the end of the script
for ind, row in train.iloc[1:10].iterrows():
    i = row['label']
    # uncomment the line below if you prefer black numbers
    # over a white background
    #arr = np.array(255 - row[1:], dtype=np.uint8)
    arr = np.array(row[1:], dtype=np.uint8)
    arr.resize((28, 28))
    plt.figure()
    plt.imshow(arr)
    #im.save("%s-%s.png" % (i, ind))
    
## create directories for output
#for i in range(10):
#    os.mkdir(str(i))
#    
#for ind, row in train.iterrows():
#    i = row['label']
#    arr = np.array(row[1:], dtype=np.uint8)
#    arr.resize((28, 28))
#    im = Image.fromarray(arr)
#    im.save("%s/%s-%s.png" % (i, i, ind))