"""
This question is asked by Facebook.
Given an array nums, return whether or not its values are monotonically increasing or monotonically decreasing.
Note: An array is monotonically increasing if for all values i <= j, nums[i] <= nums[j].
Similarly an array is monotonically decreasing if for all values i <= j, nums[i] >= nums[j].

Ex: Given the following array nums…

nums = [1, 2, 3, 4, 4, 5], return true.
Ex: Given the following array nums…

nums = [7, 6, 3], return true.
Ex: Given the following array nums…

nums = [8, 4, 6], return false.
"""


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return nums in [sorted(nums), sorted(nums, reverse=True)]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isMonotonic([1, 2, 3, 4, 4, 5]))
    print(solution.isMonotonic([7, 6, 3]))
    print(solution.isMonotonic([8, 4, 6]))
