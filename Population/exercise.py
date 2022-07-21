# APPLICATION PROCESS by STATISTA #
# Author: Tharcisio Leone #
# Dataset: Population (total) from The World Bank #

## Object: XXXX
# 0. Importing Libraries
# 1. Reading the data set
# 2. Visualise the data set
# 3. Calculate the revenue per store
# 4. Calculate the number of products sold per store
# 5. Calculate the average ticket per store
# 6. Send an email with the sales report


# 0. Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import win32com.client as win32

# 1. Reading the data set
data_popwb = pd.read_csv('Datasets\API_SP.POP.TOTL_DS2_en_csv_v2_4251154.csv', skiprows=4) # skiprows=4 will skip the first 4 lines and try to read from 5 line
#print(data_popwb)

# 2. Showing most important descriptive statistics of the data
print(list(data_popwb)) # List all columns
print('1' * 60)
print(data_popwb.info) # see first and last 5 rows
print('2' * 60)
print(data_popwb.info()) # Listing columns and (possible) missing
print('3' * 60)
print(data_popwb.describe(), round(1)) # Describing descriptive statistics
print('4' * 60)

# 3. Data handling
data_popwb2 = data_popwb.drop(['Indicator Name', 'Indicator Code'], axis = 1) # Dropping columns
print(data_popwb2)
print('5' * 60)
data_popwb3 = data_popwb2.dropna(how = 'any', axis = 0) # Dropping rows with missing
print(data_popwb3)
print('6' * 60)
print(data_popwb3.isnull().sum()) # Checking if all columns have no null values
print('7' * 60)

data_popwb4 = data_popwb3.insert(0, 'Region',['A', 'B', 'C'])
print(data_popwb4) # List all columns
print('6' * 60)

# 3. Showing total population in the world
print(data_popwb.loc[data_popwb['Country Code'] == 'WLD'])

# 4. Showing total population per income level
print(data_popwb.loc[data_popwb['Country Code'].isin(['HIC','LIC', 'LMC', 'LMY', 'MIC', 'UMC'])])

# 5. Creating graphic visualization of the evolution of population
year = [1960, 1961, 1962, 1963, 1964, 1965]
pop = [54208, 55434, 56234, 56699, 57029, 57357]
plt.plot(year, pop)
plt.title('Evolution of Population')
plt.xlabel('Year')
plt.ylabel('Number of People')
plt.show()


# 6. Creating graphic visualization with the Top 5 highest populated countries
most_popu = data_popwb.sort_values(by='2021', ascending=False).head()
plt.figure(figsize=(7,5))
sns.barplot(x='2021', y='Country Name', data=most_popu)
plt.title('Top 5 highest populated countries')
plt.xlabel('Number of People (in Billion')
plt.ylabel('Country')
plt.show()




