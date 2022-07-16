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
# 4. Reporting the number of credit card cancellation
# 5. Creating a histogram graph
# 6. Creating Looping to visualize all the graphs

# 0. Importing Libraries
import pandas as pd
import plotly.express as px


# 1. Reading the data set from Kaggle data
table_crecard = pd.read_csv('BankChurners.csv')
print(table_crecard)
print('x' * 60)


# 2. Showing most important descriptive statistics of the data
print(table_crecard.info) # see dataset info
print('n' * 60)
print(table_crecard.shape) # 10,127 rows and 23 columns
print('-' * 60)
print(table_crecard.head(5))
print(table_crecard.info()) # Listing columns and (possible) missing
print('o' * 60)
print(table_crecard.describe(), round(1)) # Describing descriptive statistics


# 3. Data handling
table_crecard2 = table_crecard.drop('CLIENTNUM', axis=1) # Dropping column
table_crecard3 = table_crecard.dropna() # Dropping rows with missing


# 4. Reporting the number of credit card cancellation
count_cust = table_crecard['Attrition_Flag'].value_counts()
print(count_cust) # 1,627 attrited customers, i.e. customers that have cancelled the credit card.

count_cust_perc = table_crecard['Attrition_Flag'].value_counts(normalize='True')
print(count_cust_perc) # 16 percent of customers have cancelled.

# Finding unique values for each columns
for columns in table_crecard:
    uniq = table_crecard[columns].value_counts()
    print(uniq, '\n============================\n')


# 5. Creating a histogram graph
graph1 = px.histogram(table_crecard, x='Customer_Age', color='Attrition_Flag')
graph1.show()


# 6. Creating Looping to visualize all the graphs
for columns in table_crecard:
    graph = px.histogram(table_crecard, x=columns, color='Attrition_Flag')
    graph.show()

# 7. Mean Conclusions
# a) The higher the number of contacts (Contacts_Count_12_mon), the higher the chance of cancellation.
# b) The higher the number and volume of transactions (Total_Trans_Ct), the lower the chance of cancellation.
