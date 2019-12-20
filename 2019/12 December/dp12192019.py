# This problem was recently asked by Amazon:

# Given a 2d n x m matrix where each cell has a certain amount of change on the floor,
# your goal is to start from the top left corner mat[0][0] and end in the bottom right corner mat[n - 1][m - 1]
# with the most amount of change. You can only move either left or down.


R = 3
C = 3
import sys


def max_change(mat, m, n):
    # Fill this in.
    if n < 0 or m < 0:
        return 0
    elif m == 0 and n == 0:
        return mat[m][n]
    else:
        return mat[m][n] + max(
            max_change(mat, m - 1, n - 1),
            max_change(mat, m - 1, n),
            max_change(mat, m, n - 1),
        )


def max(x, y, z):
    if x > y:
        return x if (x > z) else z
    else:
        return y if (y > z) else z


mat = [[0, 3, 0, 2], [1, 2, 3, 3], [6, 0, 3, 2]]
m = len(mat) - 1
n = len(mat[0]) - 1
print(max_change(mat, m, n))
# 13
