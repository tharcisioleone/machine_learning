# Author: Tharcisio Leone #
# Dataset: Coping and renaming files within the PC  #

## Maschine Learning using Linear Regression
# 0. Importing Libraries
# 1. Listing Files
# 2. Showing File Path
# 3. Renaming Files
# 4. Moving Files
# 5. Copying Files


# 0. Importing Libraries
import os
import shutil

importi shutil

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
os.rename('Sales-1new.xlsx', 'Sales\Sales-1.xlsx')

# 5. Copying Files
shutil.copy2('Sales-2.xlsx', 'Sales\Sales-2.xlsx')