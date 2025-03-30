"""
    Author: ChatGPT
    Date: 9/24/24
    Objective: ChatGPT code on how to get the Reduced Row Echelon Form
"""

import numpy as np
from sympy import Matrix

# Define the matrix
matrix = Matrix([
    [1, -3, 4, -6],
    [0, 1, -4, 4],
    [2, -4, 0, -4],
    # [-2, -7, -17, 25]
])

# Convert to Reduced Row Echelon Form (RREF)
rref_matrix, pivot_columns = matrix.rref()
the_matrix = []
counter = 0
for i in range(len(rref_matrix)):
    if i%4 == 0 or i == 0:
        the_matrix.append([])
    if i%4 == 0:
        counter += 1
    the_matrix[counter-1].append(rref_matrix[i])

for row in the_matrix:
    print(row)

print()

for row in the_matrix:
    print("|", end="")
    for element in row:
        print(element, end=" ")
    print("|")

