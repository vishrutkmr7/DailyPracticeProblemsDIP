"""
Given an integer array, nums, return the length of the longest increasing subarray.
Note: The subarray must be strictly increasing.

Ex: Given the following nums.

nums = [1, 2, 3], return 3.
Ex: Given the following nums.

nums = [3, 4, 1, 2, 8], return 3.
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS([1, 2, 3]))
    print(solution.lengthOfLIS([3, 4, 1, 2, 8]))
