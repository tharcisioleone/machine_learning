# Author: Tharcisio Leone #
# Dataset: Sales Report #

## Create a sales report and send it per e-mail
# 0. Importing Libraries
# 1. Reading the data set
# 2. Visualise the data set
# 3. Calculate the revenue per store
# 4. Calculate the number of products sold per store
# 5. Calculate the average ticket per product and store
# 6. Send an email with the sales report


# 0. Importing Libraries
import pandas as pd

# 1. Reading the data set
table_sales = pd.read_excel('Sales.xlsx')

# 2. Visualise the data set
pd.reset_option('display.max_columns', None) # Showing all the columns
print(table_sales)

# 3. Calculate the revenue per store
revenue = table_sales[['Store ID', 'Total']].groupby('Store ID').sum() # GroupBy + Filter
print(revenue)