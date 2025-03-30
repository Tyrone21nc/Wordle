"""
Author: Romain Dzeinse
Date: 4/27/24
Objective: Write code that determines one's given gender based on body composition
"""
from sklearn import tree

# [height, weight, shoe size]
x = [[181, 80, 40], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
     [159, 55, 37], [171, 75, 42], [181, 85, 43]]

y = ["male", "female", "female", "female", "male", "male", "male",
     "female", "male", "female", "male"]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x, y)
first = int(input("ENTER FIRST NUM: "))
second = int(input("ENTER SECOND NUM: "))
third = int(input("ENTER THIRD NUM: "))
prediction = clf.predict([[first, second, third]])
print(prediction)
