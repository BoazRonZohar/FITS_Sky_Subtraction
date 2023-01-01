# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:38:38 2022

@author: Lenovo
"""

import numpy as np
#import matplotlib.pyplot as plt
from astropy.io import fits
import glob


# This function substracts median from all the FTS files in the directory
def deal_with(single_filename):
    Data, Header = fits.getdata(single_filename, header=True)
    
    M = np.median(Data) # Gets Image median
    X_Max, Y_Max = np.shape(Data) # Gets Image size
    for x in range(X_Max):
        for y in range(Y_Max):
           Data[x,y] = Data[x,y]-(M-5) # substracts median - 5
    string = "Sub_"+single_filename # New File name
    fits.writeto(string, Data, Header, overwrite=True)  # writes the new substracted File
    #plt.imshow(Data, cmap='gray')
    
list_of_filenames = sorted(glob.glob('*.fts')) # creats a list of all files in the directory
print(list_of_filenames)
mylist = [deal_with(filename) for filename in list_of_filenames] # iterates through all the files in the directory

