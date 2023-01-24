"""
Given an integer array, nums, return true if for any value within nums its double also exists
within the array.

Ex: Given the following nums…

nums = [4, 3, 9, 8], return true (4 and 8 both appear in nums).
Ex: Given the following nums…

nums = [9, 2, 3, 5], return false.
"""

from collections import Counter


class Solution:
    def checkIfExist(self, nums: list[int]) -> bool:
        cnt = Counter(nums)
        return any(2 * x in cnt and x != 0 for x in nums) or cnt[0] > 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkIfExist([4, 3, 9, 8]))
    print(solution.checkIfExist([9, 2, 3, 5]))
    print(solution.checkIfExist([0, 0]))
