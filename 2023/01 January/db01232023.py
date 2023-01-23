"""
Given an array of integers, nums, and a value k, return the maximum average value
from any contiguous subarray of size k in nums.

Ex: Given the following nums and k…

nums = [4, -1, 4, 2], k = 2, return 3.0 ((4 + 2) / 2 = 3.0).
Ex: Given the following nums and k…

nums = [5, 1, -3, 5, 2], k = 3, return 1.33.
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, cur_sum)
        return max_sum / k


if __name__ == "__main__":
    print(Solution().findMaxAverage([4, -1, 4, 2], 2))
    print(Solution().findMaxAverage([5, 1, -3, 5, 2], 3))
