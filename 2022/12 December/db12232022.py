"""
Given an integer array, nums, which contains only positive integers, return whether or not nums can be partitioned into
two separate subsets such that the sum of the two subsets are equal.

Ex: Given the following nums…

nums = [1, 1, 2], return true.
Ex: Given the following nums…

nums = [10, 3, 2], return false.
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.canPartition([1, 1, 2]))
    print(solution.canPartition([10, 3, 2]))
