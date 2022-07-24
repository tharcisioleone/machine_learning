# Author: Tharcisio Leone #
# Dataset: Filling Contract Automatically  #

## Join data from two different tables
# 0. Importing Libraries
# 1. Reading the data sets
# 2. Visualise the data set
# 3. Replace one single item and save it
# 4. Filling automatically all the items

# 0. Importing Libraries
from docx import Document
from datetime import datetime
import pandas as pd

# 1. Reading the data set
document = Document('Contract.docx')
print(document)

# 2. Visualise the data set
for paragraph in document.paragraphs:
    print(paragraph.text)

# 3. Replace one single item and save it
for paragraph in document.paragraphs:
    paragraph.text = paragraph.text.replace("XXXX", "Lira")

document.save('Contract_Lira.docx')

# 4. Filling automatically all the items