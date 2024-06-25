#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:43:08 2023

@author: maitreyeedey
"""

import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%
# path = os.getcwd()

from tkinter import filedialog as tk
path = tk.askdirectory(title='Select top level data folder for "parquet" files')

#%%
all_files = glob.glob(path +  "/*.parquet")
all_files.sort() 
if(len(all_files)==0):
    raise Exception('No filles')

full_frame = []
for filename in all_files:    
    frame = pd.read_parquet(filename)
    full_frame.append(frame)

# Full table    
full_data = pd.concat(full_frame, axis = 0, ignore_index=True)

