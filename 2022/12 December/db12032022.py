"""
You are a thief trying to steal from houses in a neighborhood. The amount of money that can be
stolen from the ith house is represented by nums[i]. While you’d like to steal from all the houses,
if adjacent houses are broken into, the police are notified via a security system. Return the
largest amount of money you can steal without alerting the police.
Note: You may not modify nums. Ex: Given the following nums...

nums = [1, 3, 2, 5, 2], return 8.
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([1, 3, 2, 5, 2]))
