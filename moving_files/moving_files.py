# Author: Tharcisio Leone #
# Dataset: Coping and renaming files within the PC  #

## Maschine Learning using Linear Regression
# 0. Importing Libraries
# 1. Listing Files
# 2. Showing File Path
# 3. Renaming Files
# 4. Moving Files
# 5. Copying Files
# 6. Sorting automatically files into the respective folders


# 0. Importing Libraries
import os
import shutil

# 1. Listing Files
files = os.listdir()
print(files)
print('x'* 70)

# 2. Showing File Path
path = os.getcwd()
print(path)
print('o'* 70)

# 3. Renaming Files
#os.rename('Sales-1.xlsx', 'Sales-1new.xlsx') # To permit the code in line 29

# 4. Moving Files
#os.rename('Sales-1new.xlsx', 'Sales\Sales-1.xlsx') # To permit the code in line 36

# 5. Copying Files
#shutil.copy2('Sales-2.xlsx', 'Sales\Sales-2.xlsx')

# 6. Sorting automatically files into the respective folders
list_files = os.listdir()

for file in list_files:
    if 'xlsx' in file:
        if 'Purchases' in file: # If title contains 'Purchases', then move the file to the folder 'Purchases'
            os.rename(file, f'Purchases\{file}')
        elif 'Sales' in file: # If title contains 'Sales', then move the file to the folder 'Sales'
            os.rename(file, f'Sales\{file}')

