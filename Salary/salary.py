# Author: Tharcisio Leone #
# Dataset: Salary #

# Importing Libraries
import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt # data visualisation
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Listing all files under the input directory
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#Importing the Salary dataset (.csv file)
salary_df = pd.read_csv ('/kaggle/input/salary/Salary.csv')
salary_df


#Peeking at top 5 records of dataset
#data.head()
