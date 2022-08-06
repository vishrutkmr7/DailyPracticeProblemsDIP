"""
This question is asked by Facebook.
Given an integer array, return the sum of its contiguous sub-array that produces the largest value.
Note: Your sub-array must contain at least one value.

Ex: Given the following integer arrays…

nums = [-3,8,-8,2], return 8 (8)
nums = [2, 3,-4, 2], return 5 (2 + 3)
nums = [1, 5,-2, -3, 7], return 8 (1 + 5 + (-2) + (-3) + 7)
"""


from math import inf


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [float(-inf) for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
        return max(dp)


# Test Cases
print(Solution().maxSubArray([-3, 8, -8, 2]))
print(Solution().maxSubArray([2, 3, -4, 2]))
print(Solution().maxSubArray([1, 5, -2, -3, 7]))
