"""
Given a 2D matrix, return a list containing all of its element in spiral order.

Ex: Given the following matrix...

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], return [1, 2, 3, 6, 9, 8, 7, 4, 5].
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(solution.spiralOrder([[1, 2, 3], [4, 5, 6]]))
    print(solution.spiralOrder([[1, 2], [3, 4], [5, 6]]))
