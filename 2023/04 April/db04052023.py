"""
Given an MxN matrix, which is sorted in decreasing order (row-wise and column-wise),
return the total number of negative values in the array.

Ex: Given the following matrix…

matrix = [
  [3, -1],
  [2, -2]
], return 2 (-1 and -2 are negative).
Ex: Given the following matrix…

matrix = [
  [4, 3],
  [2, 1]
], return 0.
"""


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        total = 0
        for row in grid:
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            total += len(row) - left
        return total


# Test Cases
if __name__ == "__main__":
    matrix = [[3, -1], [2, -2]]
    print(Solution().countNegatives(matrix))
    matrix = [[4, 3], [2, 1]]
    print(Solution().countNegatives(matrix))
