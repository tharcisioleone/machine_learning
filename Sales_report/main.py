# Author: Tharcisio Leone #
# Dataset: Sales Report #

## Create a sales report and send it per e-mail
# 0. Importing Libraries
# 1. Reading the data set
# 2. Calculate the revenue per store
# 3. Calculate the number of products sold per store
# 4. Calculate the average ticket per product and store
# 5. Send an email with the sales report


# 0. Importing Libraries
import pandas as pd

# 1. Reading the data set
table_sales = pd.read.excel('Sales.slsx')