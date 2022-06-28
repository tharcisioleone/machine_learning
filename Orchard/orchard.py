# Author: Tharcisio Leone #
# Dataset: Orchard #

## Maschine Learning using Decision Trees
# 0. Importing Libraries
# 1. Reading the data set from Kaggle data.
# 2. Showing the first five rows of the data set.

# 0. Importing Libraries
from sklearn import tree

# 1. Transforming string in dummy
red = 1
yellow = 0
apple = 1
banana = 0

# 2. Creating the database
orchard = [[150, red], [130, red], [180, yellow], [160, yellow]]
output = [apple, apple, banana, banana]

# 3. Imputing Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(orchard, output)

# 4. Including the questions to be imputed.
weight = input('Please typ the weight of the fruit: ')
color = input('Please typ the color of the fruit: ')

# 5. Showing results of the Decision Tree
answeruser = clf.predict([[weight, color]])

if answeruser == 1:
    print('This is a Apple')
else:
    print('This is a Banana')
