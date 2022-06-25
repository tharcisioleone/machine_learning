# Author: Tharcisio Leone #
# Dataset: Salary #

## Maschine Learning using Linear Regression
# 0. Importing Libraries
# 1. Reading the data set from Kaggle data.
# 2. Showing the first five rows of the data set.
# 3. Showing the correlation across the variables.
# 4. Exporting the correlation matrix to CSV file.
# 5. Showing correlation in a graph (Scotter Plot).
# 6. Using a regression model, split the data into train and test portions.
# 7. Fitting the training split to the regression model.
# 8. Showing the regression model’s score.
# 9. Drawing at least three conclusions from the regression model.


# 0. Importing Libraries.
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Reading the data set from Kaggle data.
salary_df = pd.read_csv ('C:/Users/tharc/Documents/GitHub/machine_learning/Salary/Salary.csv')

# 2. Showing the first five rows of the data set.
print(salary_df.shape) # 35 rows and 2 columns
print(salary_df.head(5))

# 3. Showing the correlation across the variables.
cor_2=salary_df.corr()
print(cor_2)

# 4. Exporting the correlation matrix to CSV file.
df_2=pd.DataFrame(cor_2)
df_2.to_csv('C:/Users/tharc/Documents/GitHub/machine_learning/Salary/correlation.cvs')

# 5. Showing correlation in a graph (Scotter Plot).
x=salary_df['YearsExperience']
y=salary_df['Salary']
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.scatter(x,y)
plt.show()

# 6. Using a regression model, split the data into train and test portions.
yrs = salary_df['YearsExperience'].values
sal = salary_df['Salary'].values
yrs_exp_vector= yrs.reshape(-1, 1)
print(yrs_exp_vector)

xtrain, xtest, ytrain, ytest = train_test_split(yrs_exp_vector, sal, train_size = 8, test_size=.2)
print(xtrain)

# 7. Fitting the training split to the regression model.
plt.scatter(xtrain, ytrain, color = 'purple')
plt.xlabel("Years of Experience")
plt.ylabel("Salary in $")
plt.title("Training Data")train = pd.read_csv("../input/train.csv")
test = pd.read_csv("../input/test.csv")
pred = pd.read_csv("../input/sampleSubmission.csv")

train.drop(["casual", "registered"], axis=1, inplace=True)
plt.show()

# 8. Showing the regression model’s score.
lm = LinearRegression()
lm.fit(xtrain, ytrain)
y_predict = lm.predict(xtest)
print(f"Train accuracy {round(lm.score(xtrain,ytrain)*100,2)}%")
print(f"Test accuracy {round(lm.score(xtest,ytest)*100,2)}%")


# 9. Drawing at least three conclusions from the regression model.
# After 7 years salary stays pretty stable until the people reach 14 years then it increases significantly
# Between 2-5 years of experience the salary does not change very much.
# It seems that 4-10 years of experience is ideal for most employers.