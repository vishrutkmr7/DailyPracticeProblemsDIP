"""
Given a two-dimensional NxN integer array, matrix, return the sum of all values along its two diagonals.
Note: If a value appears in both diagonals it should only be added to your sum once.

Ex: Given the following matrix…

matrix = [
  [1, 2],
  [2, 1]
], return 6 (1 + 1 + 2 + 2).
Ex: Given the following matrix…

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], return 25 (5 is only added to the sum once).
"""


class Solution:
    def diagonalSum(self, matrix: list[list[int]]) -> int:
        res = 0
        for i, v in enumerate(matrix):
            res += v[i]
            res += v[len(matrix) - i - 1]

        if len(matrix) % 2 == 1:
            res -= matrix[len(matrix) // 2][len(matrix) // 2]
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.diagonalSum([[1, 2], [2, 1]]))
    print(solution.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
