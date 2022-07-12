# Author: Tharcisio Leone #
# Dataset: Credit Card customers #

# Challenge: https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers
# A manager at the bank is disturbed with more and more customers leaving their credit card services.
# They would really appreciate if one could predict for them who is gonna get churned. So they can proactively
# go to the customer to provide them better services and turn customers' decisions in the opposite direction.

## Maschine Learning using Python
# 0. Importing Libraries
# 1. Reading the data set from Kaggle data
# 2. Showing most important descriptive statistics of the data
# 3. Data handling
# 4. Creating a data analysis to identify the main reasons for the credit card cancellation

# 0. Importing Libraries
import pandas as pd

# 1. Reading the data set from Kaggle data
table_crecard = pd.read_csv('BankChurners.csv')
print(table_crecard)

# 2. Showing most important descriptive statistics of the data
print(table_crecard) # 5 rows and 10 columns
print(table_crecard(5))

# 3. Data handling
table_crecard = table_crecard.drop('CLIENTNUM', axis=1)
