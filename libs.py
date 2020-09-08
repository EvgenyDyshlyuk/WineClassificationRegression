# Create a file allowing to import upper level(usefull throughout the whole solution) packages and functions with one line: %run libraries

import os #The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on 

import pickle # Fast saving/loading data

import numpy as np

import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

# Import visualizations
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20,5) # Set standard output figure size

import seaborn as sns # sns visualization library

from IPython.display import display # Allows to nicely display/output several figures or dataframes in one cell

import lightgbm as lgb

import shap # Calculate feature importance for tree-based algorithms

print('libraries loaded')

from sklearn.model_selection import train_test_split