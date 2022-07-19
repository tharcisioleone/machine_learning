# Author: Tharcisio Leone #
# Dataset: Coping and renaming files within the PC  #

## Maschine Learning using Linear Regression
# 0. Importing Libraries
# 1. Listing Files
# 2. Including File Path
# 3. Renaming Files
# 4. Copying Files


# 0. Importing Libraries
import os

# 1. Listing Files
files = os.listdir()
print(files)

# 2. Including File Path
path = os.getcwd()
print(path)