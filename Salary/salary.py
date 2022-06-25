# Author: Tharcisio Leone #
# Dataset: Salary #

## Using Linear Regression for Maschine Learning
# 0. Importing Libraries
# 1. Select a Kaggle data set that is suitable for Linear Regression.
# 2. Show the first five rows of the data set.
# 3. Show the description and the info of the data set.
# 4. Using a regression model, split the data into train and test portions.
# 5. Fit the training split to the regression model.
# 6. Show the regression model’s score.
# 7. Draw at least three conclusions from the regression model.


# 0. Importing Libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# 1. Select a Kaggle data set that is suitable for Linear Regression.
salary_df = pd.read_csv ('/kaggle/input/salary/Salary.csv')
salary_df

# 2. Show the first five rows of the data set.
salary_df[:5]

# 3. Show the description and the info of the data set.
salary_df.describe()

# 4. Using a regression model, split the data into train and test portions.
yrs = salary_df['YearsExperience'].values
sal = salary_df['Salary'].values
yrs_exp_vector= yrs.reshape(-1, 1)
yrs_exp_vector


xtrain, xtest, ytrain, ytest = train_test_split(yrs_exp_vector, sal, train_size = 8, test_size=.2)
xtrain


# 5. Fit the training split to the regression model.
plt.scatter(xtrain, ytrain, color = 'purple')
plt.xlabel("Years of Experience")
plt.ylabel("Salary in $")
plt.title("Training Data")
plt.show()


# 6. Show the regression model’s score.
lm = LinearRegression()
lm.fit(xtrain, ytrain)
y_predict = lm.predict(xtest)
print(f"Train accuracy {round(lm.score(xtrain,ytrain)*100,2)}%")
print(f"Test accuracy {round(lm.score(xtest,ytest)*100,2)}%")



# 7. Draw at least three conclusions from the regression model.
# After 7 years salary stays pretty stable until you reach 14 years then it increases significantly
# Between 2-5 years of experience the salary does not change very much.
# It seems that 4-10 years of experience is ideal for most employers.

