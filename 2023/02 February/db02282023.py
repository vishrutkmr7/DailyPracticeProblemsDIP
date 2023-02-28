"""
Given a binary matrix, return the number of lonely indices.
Note: An index (i, j) is lonely if matrix[i][j] is equal to one and all other elements in the ith row and jth
column are zeroes.

Ex: Given the following matrix…

matrix = [
  [1, 0],
  [0, 1]
], return 2.
Ex: Given the following matrix…

matrix = [
  [1, 0, 1],
  [0, 1, 0],
  [0, 0, 1]
], return 1.
"""


class Solution:
    def countLonely(self, matrix: list[list[int]]) -> int:
        count = 0
        for item in matrix:
            for j in range(len(matrix[0])):
                if (
                    item[j] == 1
                    and sum(item) == 1
                    and sum(matrix[k][j] for k in range(len(matrix))) == 1
                ):
                    count += 1
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.countLonely([[1, 0], [0, 1]]))
    print(solution.countLonely([[1, 0, 1], [0, 1, 0], [0, 0, 1]]))
