# Author: Tharcisio Leone #
# Dataset: Orchard #

## Maschine Learning using Decision Trees
# 0. Importing Libraries
# 1. Transforming string in dummy
# 2. Creating the data
# 3. Imputing Decision Tree
# 4. Including the questions to be imputed
# 5. Showing results of the Decision Tree

# 0. Importing Libraries
from sklearn import tree

# 1. Transforming string in dummy (sklearn does not work with string)
red = 1
yellow = 0
apple = 1
banana = 0

# 2. Creating the data
train_x = [[150, red], [130, red], [180, yellow], [160, yellow]]
train_y = [apple, apple, banana, banana]

# 3. Imputing Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_x, train_y)

# 4. Including the questions to be imputed
weight = input('Please type the weight of the fruit: ')
color = input('Please type the color of the fruit (1 for red and 0 for yellow): ')

# 5. Showing results of Decision Trees
answeruser = clf.predict([[weight, color]])

if answeruser == 1:
    print('This is a Apple !!')
else:
    print('This is a Banana !!')
