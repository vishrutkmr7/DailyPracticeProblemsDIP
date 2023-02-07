"""
You are given an integer array, nums, which contains 2N elements. Within nums there are N + 1 unique elements and a specific
element occurs N times. Return the element within nums that appears N times.

Ex: Given the following nums…

nums = [3, 3, 5, 1], return 3.
Ex: Given the following nums…

nums = [4, 2, 4, 5, 4, 1], return 4.
"""


class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        for i, v in enumerate(nums):
            if v in nums[i + 1 :]:
                return v


# Test Cases
print(Solution().repeatedNTimes([3, 3, 5, 1]))
print(Solution().repeatedNTimes([4, 2, 4, 5, 4, 1]))
