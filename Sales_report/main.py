# Author: Tharcisio Leone #
# Dataset: Sales Report #

## Create a sales report and send it per e-mail
# 0. Importing Libraries
# 1. Reading the data set
# 2. Visualise the data set
# 3. Calculate the revenue per store
# 4. Calculate the number of products sold per store
# 5. Calculate the average ticket per store
# 6. Send an email with the sales report


# 0. Importing Libraries
import pandas as pd
import win32com.client as win32

# 1. Reading the data set
table_sales = pd.read_excel('Sales.xlsx')

# 2. Visualise the data set
pd.reset_option('display.max_columns', None) # Showing all the columns
print(table_sales)
print('-' * 50) # For a better visualisation of the tables

# 3. Calculate the revenue per store
revenue = table_sales[['Store ID', 'Total']].groupby('Store ID').sum() # GroupBy + Filter
print(revenue)
print('-' * 50) # For a better visualisation of the tables

# 4. Calculate the number of products sold per store
quantity = table_sales[['Store ID', 'Quantity']].groupby('Store ID').sum()
print(quantity)
print('-' * 50) # For a better visualisation of the tables

# 5. Calculate the average ticket per store
# average ticket = revenue / quantity
average_ticket = (revenue['Total'] / quantity['Quantity']).to_frame()
average_ticket = average_ticket.rename(columns={0:'Average Ticket'})
print(average_ticket)

# 6. Send an email with the sales report
# Copy and paste code from Stackoverflow: https://stackoverflow.com/questions/6332577/send-outlook-email-via-python
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'tharcisioleone@gmail.com'
mail.Subject = 'Sales Report'
mail.Body = f'''
<p>Dear colleagues,</p>
<p>please find attached the most recent sales report divided by stores.</p>

<p>Table 1: Revenue per store</p>
{revenue.to_html(formatter={'Total': 'EUR{:,.2f}'.format})}

<p>Table 2: Number of products sold per store</p>
{quantity.to_html()}

<p>Table 3: Average ticket per store</p>
{average_ticket.to_html(formatter={'Average Ticket': 'EUR{:,.2f}'.format})}

<p>Please let me know if you need any further information.</p>
<p>Best regards,</p>
<p>Tharcisio Leone</p>
'''

mail.Send()
print(Email has been sent.)