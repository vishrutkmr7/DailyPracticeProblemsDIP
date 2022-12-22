"""
Given an N x M matrix, containing distinct elements, return all special values.
Note: A special value in the matrix is an element that is the minimum element in the its row and the maximum element in
its column.

Ex: Given the following matrix…

matrix = [
  [1, 2],
  [3, 4]
], return [3].
Ex: Given the following matrix…

matrix = [
  [1, 2, 5],
  [4, 8, 3],
  [9, 7, 6]
], return [6].
"""


class Solution:
    def specialValues(self, matrix: list[list[int]]) -> list[int]:
        special_values = []
        for item in matrix:
            special_values.extend(
                item[column]
                for column in range(len(item))
                if item[column] == min(item)
                and item[column] == max(matrix[i][column] for i in range(len(matrix)))
            )
        return special_values


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.specialValues([[1, 2], [3, 4]]))
    print(solution.specialValues([[1, 2, 5], [4, 8, 3], [9, 7, 6]]))
