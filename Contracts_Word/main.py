# Author: Tharcisio Leone #
# Dataset: Filling Contract Automatically  #

## Join data from two different tables
# 0. Importing Libraries
# 1. Reading the data sets
# 2. Visualise the data set


# 0. Importing Libraries
import pandas as pd
import openpyxl as opy
from docx import Document

# 1. Reading the data set
document = Document('Contract.docx')
print(document)

# 2. Visualise the data set
for paragraph in document.paragraphs:
    print(paragraph.text)

