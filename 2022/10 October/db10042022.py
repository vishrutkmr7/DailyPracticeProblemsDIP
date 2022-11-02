"""
Given a 2D matrix nums, return the matrix transposed.
Note: The transpose of a matrix is an operation that flips each value in the matrix across its main diagonal.

Ex: Given the following matrix nums…

nums = [
  [1, 2],
  [3, 4]
]
return a matrix that looks as follows...
[
  [1,3],
  [2,4]
]
"""
import numpy


class Solution:
    def transpose(self, nums: list[list[int]]) -> list[list[int]]:
        return numpy.transpose(nums).tolist()


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    print("All tests passed.")
