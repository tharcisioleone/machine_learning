# Author: Tharcisio Leone #
# Dataset: Join Tables #

## Join data from two different tables
# 0. Importing Libraries
# 1. Reading the data sets
# 2. Visualise the data set
# 3. Calculate the revenue per store
# 4. Calculate the number of products sold per store
# 5. Calculate the average ticket per store
# 6. Send an email with the sales report


# 0. Importing Libraries
import pandas as pd

# 1. Reading the data sets
table_python = pd.read_excel('Table2.xlsx')
table_datascience = pd.read_excel('Table1.xlsx')