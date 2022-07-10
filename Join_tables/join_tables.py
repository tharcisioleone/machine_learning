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
print(table_python)
print(table_datascience)
print('-' * 70)

# 2. Joining both tables
# See background: https://pandas.pydata.org/docs/user_guide/merging.html#:~:text=pandas%20provides%20various%20facilities%20for,join%20%2F%20merge%2Dtype%20operations.
table_pytdata = pd.concat([table_python, table_datascience], keys=['Table2', 'Table1']) # Alternativ: ignore_index=True
print(table_pytdata)
