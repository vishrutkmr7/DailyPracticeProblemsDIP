"""
Given an integer array, nums, and a value, k, return the total number of contiguous subarrays
that are divisible by k.

Ex: Given the following nums and k…

nums = [1, 3, 1, 2, 5], k = 7, return 2 ([1, 3, 1, 2] and [2, 5] both sum to 7).
"""


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res, running_sum = 0, 0
        dp = [1] + [0] * k
        for num in nums:
            running_sum += num
            res += dp[running_sum % k]
            dp[running_sum % k] += 1
        return res


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.subarraysDivByK([1, 3, 1, 2, 5], 7) == 2
    print("Passed all tests!")
