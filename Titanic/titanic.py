# Author: Tharcisio Leone #
# Dataset: Titanic #

## Maschine Learning for Data Analysis
## Step 0: Importing Libraries
## Step-2 EDA
## Step-3 Data Preparation
## Step 4: Splitting the Data into Training and Testing Sets
## Step-5 Building model using statsmodel, for the detailed statistics



## Step 0: Importing Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import warnings
warnings.filterwarnings('ignore')


## Step 1: Reading and Understanding the Data
#Importing the data
train_data= pd.read_csv("../input/titanic/train.csv")
train_data.head()

# Data Preparation
train_data.shape

# Checking if there is any null values
train_data.isnull().sum()

# Handling missing values
null_values = round(train_data.isnull().sum()*100/len(train_data),2)
null_values

# We will drop column cabin as it has more than 50% null values
train_data=train_data.drop(["Cabin"],axis=1)
train_data.head()
train_data.describe()

median=train_data["Age"].median()
train_data["Age"].fillna(median,inplace=True)

train_data.isnull().sum()

mode=train_data["Embarked"].mode()[0]
train_data["Embarked"].fillna(mode,inplace=True)

train_data.isnull().sum()

train_data.describe()

train_data.nunique()

id_cols=["PassengerId","Name","Ticket"]
cate_cols=["Survived","Pclass","Sex","SibSp","Parch","Embarked"]
con_cols=["Age","Fare"]

# remove unnecessory columns
train_data.drop(id_cols,axis=1,inplace=True)

train_data.head()

train_data.Sex=train_data.Sex.map({"male":0,"female":1})
train_data.head()


# Outlier Handling

# Analyse data
for i in con_cols:
    print(i)
    sns.boxplot(train_data[i])
    plt.show()

# Handling outliers for Age column
train_data["Age"].describe()

q1=22
q3=35
iqr=q3-q1
lower_bound=q1-1.5*iqr
upper_bound=q3+1.5*iqr
train_data["Age"]=np.where(train_data["Age"]>upper_bound,upper_bound,train_data["Age"])
train_data["Age"]=np.where(train_data["Age"]<lower_bound,lower_bound,train_data["Age"])

# Handling outliers for Fare column
train_data["Fare"].describe()


q1=7.910400
q3=31
iqr=q3-q1
lower_bound=q1-1.5*iqr
upper_bound=q3+1.5*iqr
train_data["Fare"]=np.where(train_data["Fare"]>upper_bound,upper_bound,train_data["Fare"])
train_data["Fare"]=np.where(train_data["Fare"]<lower_bound,lower_bound,train_data["Fare"])


## Step-2 EDA

for i in cate_cols:
    sns.countplot(train_data[i])
    plt.title(i)
    plt.show()

# Creating pairplot for continous variables
sns.pairplot(train_data[con_cols])
plt.show()

# Insight: There is no correlation between Age and Fare.

plt.figure(figsize=(12,8))
sns.heatmap(train_data.corr(),annot=True,cmap="YlGnBu")
plt.show()

# Insight: Fare column is highly correlated with Survived & Pclass column is negatively correlated with Survived.
train_data.head()


## Step-3 Data Preparation

# Dummy Creation
train_data.info()

# Creating dummy variables for column Embarked
train_data["Pclass"]=train_data["Pclass"].astype('object')
train_data["SibSp"]=train_data["SibSp"].astype('object')
train_data["Parch"]=train_data["Parch"].astype('object')

cols=["Pclass","SibSp","Parch","Embarked"]
dummies=pd.get_dummies(train_data[cols],drop_first=True)
train_data1=pd.concat([train_data,dummies],axis=1)

dummies

train_data1=train_data1.drop(cols,axis=1)

train_data1

train_data1.shape


## Step 4: Splitting the Data into Training and Testing Sets

X=train_data1.drop(["Survived"],axis=1)
Y=train_data1[["Survived"]]

# Scaling
X=(X-X.mean())/X.std()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,train_size=0.7,test_size=0.3,random_state=100)

print("X_train Shape:", X_train.shape)
print("Y_train Shape:", y_train.shape)
print("X_test Shape:", X_test.shape)
print("Y_test Shape:", y_test.shape)

# Feature selection
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

estimator=LogisticRegression()
estimator.fit(X_train,y_train)

selector=RFE(estimator,n_features_to_select=10)
selector=selector.fit(X_train,y_train)

list(zip(X_train.columns,selector.support_,selector.ranking_))

selector=selector.fit(X_train,y_train)
selector.support_

cols_retain=list(X_train.columns[selector.support_])

X_train=X_train[cols_retain]
X_test=X_test[cols_retain]

X_train.shape




## Step-5 Building model using statsmodel, for the detailed statistics

# Model-1
import statsmodels.api as sm
X_train_sm=sm.add_constant(X_train)
X_test_sm=sm.add_constant(X_test,has_constant="add")
print(X_train_sm.shape,X_test_sm.shape)
model1=sm.GLM(y_train,X_train_sm,family=sm.families.Binomial()).fit()
model1.summary()

# Model-2
X_train_sm=X_train_sm.drop(["SibSp_5"],axis=1)
X_test_sm=X_test_sm.drop([],axis=1)
model2=sm.GLM(y_train,X_train_sm,family = sm.families.Binomial()).fit()
model2.summary()

# Model-3
X_train_sm=X_train_sm.drop(["SibSp_8"],axis=1)
X_test_sm=X_test_sm.drop([],axis=1)
model3=sm.GLM(y_train,X_train_sm,family=sm.families.Binomial()).fit()
model3.summary()
