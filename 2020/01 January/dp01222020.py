#  This problem was recently asked by Twitter:

# Given a matrix, transpose it. Transposing a matrix means the rows are now the column and vice-versa.


def transpose(mat):
    # Fill this in.
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]


mat = [[1, 2, 3], [4, 5, 6]]

print(transpose(mat))
# [[1, 4],
#  [2, 5],
#  [3, 6]]

# numpy.transpose()
