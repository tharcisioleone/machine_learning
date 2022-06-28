
# Author: Tharcisio Leone #
# Dataset: Bike Sharing Demand #

## Maschine Learning using Linear Regression
# 0. Importing Libraries
# 1. Reading the data set from Kaggle data.
# 2. Showing the first five rows of the data sets.
# 3. Calculating the Mean Absolute Error
# 4. Putting MAE in relation to a basis prediction
# 5. Including additional variables necessary for the prediction
# 6. Displaing graphically the bike demand over the day



# 0. Importing Libraries
import lightgbm as lgb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics

plt.style.use('ggplot')


# Instead of matplotlib inline: Because the notebook needs to be convertable to a Python script where IPython magic does not work.
import matplotlib.pyplot as pl
try:
    get_ipython().magic("matplotlib inline")
except:
    pl.ion()


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

def score(pred): #  Calling score the method computes the accuracy score by default.
    solution = pd.read_csv("C:/Users/tharc/Documents/GitHub/machine_learning/Bike/solution.csv").cnt
    return MAE(solution, pred)

mae_example = pd.DataFrame({"real": [10,10,25], "prediction": [5,15,5]})
mae_example["Absolute Error"] = np.abs(mae_example.prediction - mae_example.real)
print(mae_example)

print(MAE(mae_example.real, mae_example.prediction)) # MAE = 10





############### (WORK IN PROGRESS) ################################
# 4. Putting MAE in relation to a basis prediction

pred["cnt"] = 0 # Rent number is assumed as 0 as example only.
score(pred.cnt)
print(score(pred.cnt)) # 185.92 is the maximal MAE that you can have. In case of all predictions = 0.



pred["cnt"] = train.cnt.mean() # Rent number is the mean value
print(score(pred.cnt))



# 5. Creating additional variables to improve the prediction
df = pd.concat([train, test], sort=False)
df.datetime = pd.to_datetime(df.datetime)

df["hour"] = df.datetime.dt.hour
df["dow"] = df.datetime.dt.weekday # weekday_name
df["weekend"] = (df.dow >= 5).astype(int)

print(df.head(10))



# 6. Displaing graphically the bike demand over the day
df[df.cnt.notnull()].groupby(["hour", "weekend"]).cnt.mean().unstack().plot(figsize=(20, 9))
plt.pyplot.show()


# 7. Including the additional variables into the prediction to improve the MAE.
train = df[df.cnt.notnull()]
y_train = train.cnt
X_train = train.drop(["datetime", "cnt"], axis=1)
X_test = df[df.cnt.isnull()].drop(["datetime", "cnt"], axis=1)

mean_by_weekend_hour = train.groupby(["weekend", "hour"]).cnt.mean()
joined = X_test.join(mean_by_weekend_hour, on=["weekend", "hour"], how="left")
print(joined[joined.weekend == 0].head())


pred["cnt"] = joined.cnt
print(score(pred.cnt)) # MAE decreases to 77.16.


# 8. Including Machine Learning ##
df_lgb = lgb.Dataset(X_train, label=y_train)
params = {"objective": "mae"} # Imputing algorithms
model = lgb.train(params, df_lgb) # Imputing Decision trees

pred["cnt"] = model.predict(X_test)
print(score(pred.cnt)) # # MAE decreases to 50.14.



