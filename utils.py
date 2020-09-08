import os
import pandas as pd

def df_info(df):
    print('-------------------------------------------shape----------------------------------------------------------------')
    print(df.shape)
    print('-------------------------------------head() and tail(1)---------------------------------------------------------')
    display(df.head(), df.tail(1))
    print('------------------------------------------nunique()-------------------------------------------------------------')
    print(df.nunique())
    print('-------------------------------------describe().round()---------------------------------------------------------')
    print(df.describe().round())
    print('--------------------------------------------info()--------------------------------------------------------------')
    print(df.info())
    print('-------------------------------------------isnull()-------------------------------------------------------------')
    print(df.isnull().sum())
    print('--------------------------------------------isna()--------------------------------------------------------------')
    print(df.isna().sum())
    print('-----------------------------------------duplicated()-----------------------------------------------------------')
    print(len(df[df.duplicated()]))
    print('----------------------------------------------------------------------------------------------------------------') 

def create_directory_structure():
    # Create an output' folder to save data from the notebook
    try:
        os.mkdir('input')  # Try to create
    except FileExistsError:
        pass  # if already exist pass

    # Create an output' folder to save data from the notebook
    try: os.mkdir('output') # Try to create
    except FileExistsError: pass # if already exist pass

    # Create 'data' folder in the 'output' folder
    try: os.mkdir(r'output/data')
    except FileExistsError: pass
    # Create 'submissions' folder in the 'output' folder
    try: os.mkdir(r'output/submissions')
    except FileExistsError: pass
    # Create 'models' folder in the 'output' folder
    try: os.mkdir(r'output/models')
    except FileExistsError: pass
    # Create 'predicts' folder in the 'output' folder
    try:os.mkdir(r'output/predicts')
    except FileExistsError: pass

def create_journal():
    # Create Experimental Journal, for experiments tracking
    from os.path import exists
    if exists('Journal.csv'):
        pass
    else:
        row = 'Test name, RMSE_train, RMSE_val, RMSE_Public, Comments'
        with open('Journal.csv','a') as file:
            file.write(row)

