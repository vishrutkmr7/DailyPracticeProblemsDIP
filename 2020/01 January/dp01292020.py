#  This problem was recently asked by Facebook:

# Reshaping a matrix means to take the same elements in a matrix but change the row and column length.
# This means that the new matrix needs to have the same elements filled in the same row order as the old matrix.
# Given a matrix, a new row size x and a new column size y, reshape the matrix. If it is not possible to reshape, return None.

import numpy as np


def reshape_matrix(mat, x, y):
    # Fill this in.
    try:
        return np.reshape(mat, (y, x))
    except ValueError:
        return None


print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
