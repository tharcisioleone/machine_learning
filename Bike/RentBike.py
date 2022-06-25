
# Author: Tharcisio Leone #
# Dataset: Rent a Bike #

## Maschine Learning using Linear Regression
# 0. Importing Libraries
# 1. Reading the data set from Kaggle data.
# 2. Showing the first ten rows of the data set.



# 0. Importing Libraries
import lightgbm as lgb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics

plt.style.use('ggplot')

#get_ipython().magic('matplotlib inline')


# 1. Reading the data set from Kaggle data.
train = pd.read_csv("C:/Users/tharc/Documents/GitHub/machine_learning/Bike/train.csv")
test = pd.read_csv("C:/Users/tharc/Documents/GitHub/machine_learning/Bike/test.csv")
pred = pd.read_csv("C:/Users/tharc/Documents/GitHub/machine_learning/Bike/sampleSubmission.csv")

train.drop(["casual", "registered"], axis=1, inplace=True)


# 2. Showing the first five rows of the data sets.
print(train.shape) # 5 rows and 10 columns
print(train.head(5))
print(test.head(5))
print(pred.head(5))


# 3. Calculating the Mean Absolute Error
def MAE(actual, pred):
    return metrics.mean_absolute_error(actual, pred)

def score(pred):
    solution = pd.read_csv("C:/Users/tharc/Documents/GitHub/machine_learning/Bike/solution.csv").cnt
    return MAE(solution, pred)

mae_example = pd.DataFrame({"real": [10,10,25], "prediction": [5,15,5]})
mae_example["Absolute Error"] = np.abs(mae_example.prediction - mae_example.real)
print(mae_example)

print(MAE(mae_example.real, mae_example.prediction)) # MAE = 10

