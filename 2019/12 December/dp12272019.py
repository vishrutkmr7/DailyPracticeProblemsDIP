# This problem was recently asked by Uber:

# Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.


def rotate(mat):
    # Fill this in.
    N = len(mat[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[N - 1 - j][i]
            mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j]
            mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i]
            mat[j][N - 1 - i] = temp

    return mat


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Looks like
# 7 4 1
# 8 5 2
# 9 6 3
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
