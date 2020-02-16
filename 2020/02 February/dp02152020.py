#  This problem was recently asked by Facebook:

# Given a matrix that is organized such that the numbers will always be sorted left to right,
# and the first number of each row will always be greater than the last element of the last row (mat[i][0] > mat[i - 1][-1]),
# search for a specific value in the matrix and return whether it exists.


def searchMatrix(mat, value):
    # Fill this in.
    for sub in mat:
        if value > sub[len(sub) - 1]:
            continue
        else:
            return value in sub


mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
