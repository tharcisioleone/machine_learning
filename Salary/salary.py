# Author: Tharcisio Leone #
# Dataset: Salary #

## Using Linear Regression for Maschine Learning
# 0. Importing Libraries
# 1. Get the data.
# 2. Discover and visualize the data to gain insights.
# 3. Prepare the data for Machine Learning algorithms.
# 4. Select a model and train it.
# 5. Fine-tune your model.
# 6. Present your solution.
# 7. Launch, monitor, and maintain your system.


# 0. Importing Libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# 1. Get the data
data = pd.read_csv('/kaggle/input/salary/Salary.csv')
data.head()

# 2. Discover and visualize the data to gain insights.
data.info()

# Insights
# 1. No null values
# 2. Years of experience is float but salary is integer

# 3. Discover and visualize the data to gain insights.
plt.plot(data['YearsExperience'],data['Salary'],'.')
plt.show()

# Insights:
#  1. I/p and O/p has linear model, linear regression can be good and simple option

# 4. Discover and visualize the data to gain insights.
plt.hist(data['YearsExperience'],bins=4)
plt.show()

#Insights:
# 1. We have high number of data points for YearsExperience in range 1 to 4 yrs
# 2. To create test dataset, random sampling should be avoided as it can create sample bias
# 3. We will use stratified sampling, which tries to keep same distribution profile as actual data.

# 5. Prepare the data for Machine Learning algorithms.

# Splitting data into train and test data (using stratified sampling)
data["YearsExp_dist"] = pd.cut(data["YearsExperience"],bins=[0.0, 2.5, 4.0, 7.5, 11.0, np.inf],labels=[1, 2, 3, 4,5])
data["YearsExp_dist"].hist()
# We will use below distribution for stratified sampling

# Using scikit for stratified sampling
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42) # split into 80%-20% ratio
for train_index, test_index in split.split(data, data["YearsExp_dist"]):
    train_set = data.loc[train_index]
    test_set = data.loc[test_index]
type(train_set)
plt.plot(train_set['YearsExperience'],train_set['Salary'],'g*',test_set['YearsExperience'],test_set['Salary'],'r*')
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.legend(['train_set','test_set'])


#Only for curiosity, lets also try random sampling for splitting train and test data
from sklearn.model_selection import train_test_split
random_sampling_train_set, random_sampling_test_set = train_test_split(data, test_size=0.2,random_state=14)
plt.plot(random_sampling_train_set['YearsExperience'],random_sampling_train_set['Salary'],'g*',random_sampling_test_set['YearsExperience'],random_sampling_test_set['Salary'],'r*')
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.legend(['train_set','test_set'])
# If we compare o/p of stratified sampling to random sampling's o/p, the stratified sampling gives well distributed test set.
# Though due to linear relationship this may not be problem, but in case of non-linear data this can create problem

X_train = train_set.drop(['YearsExp_dist','Salary'],axis=1)
y_train = train_set.drop(['YearsExperience','YearsExp_dist'],axis=1)
X_test  = test_set.drop(['YearsExp_dist','Salary'],axis=1)
y_test = test_set.drop(['YearsExperience','YearsExp_dist'],axis=1)
#X_train.head()
#y_train.head()

# Training our model using Linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
lin_reg.predict(X_test)


# Model
# Intecept and coeff of the line
print('Intercept of the model:',lin_reg.intercept_)
print('Coefficient of the line:',lin_reg.coef_)

# Checking performance over Training dataset
from sklearn.metrics import mean_squared_error
y_train_predictions = lin_reg.predict(X_train)
lin_mse = mean_squared_error(y_train, y_train_predictions)
lin_rmse_train = np.sqrt(lin_mse)
lin_rmse_train


# Performance plot
plt.plot(X_train,y_train,'r*',X_train,y_train_predictions,'g*')


# Checking performance over Test dataset
from sklearn.metrics import mean_squared_error
y_predictions = lin_reg.predict(X_test)
lin_mse = mean_squared_error(y_test, y_predictions)
lin_rmse = np.sqrt(lin_mse)
lin_rmse


# Performance plot
plt.plot(X_test,y_test,'r*',X_test,y_predictions,'g*')


