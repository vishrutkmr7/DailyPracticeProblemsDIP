"""Given a two-dimensional integer array, matrix, return whether or not the matrix is a Toeplitz matrix.
Note: A Toeplitz matrix is a matrix in which every diagonal from the top-left corner to the bottom-right
hand corner of the matrix contains the same element. 

Ex: Given the following matrix…

matrix = [
  [1, 2, 3],
  [4, 1, 2],
  [5, 4, 1]
], return true ([4, 4], [1, 1, 1], and [2, 2] are the diagonals and each diagonal has the same element).
Ex: Given the following matrix…

matrix = [
  [1, 2],
  [3, 4]
], return false.
"""


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(matrix, matrix[1:]))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isToeplitzMatrix([[1, 2, 3], [4, 1, 2], [5, 4, 1]]))
    print(solution.isToeplitzMatrix([[1, 2], [3, 4]]))
