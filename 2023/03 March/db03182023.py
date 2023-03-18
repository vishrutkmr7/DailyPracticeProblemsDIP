"""
Given an array of positive integers, nums, return the largest sum we can create such that it is
divisible by three.

Ex: Given the following nums…

nums = [3, 1, 5, 8, 2], return 18 (3 + 5 + 8 + 2).
Ex: Given the following nums…

nums = [2, 4, 9], return 15.
"""


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp = [0] * 3
        for num in nums:
            for i in dp[:]:
                dp[(i + num) % 3] = max(dp[(i + num) % 3], i + num)
        return dp[0]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumDivThree([3, 1, 5, 8, 2]))
    print(solution.maxSumDivThree([2, 4, 9]))
