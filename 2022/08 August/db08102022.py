"""
This question is asked by Google.
Given a staircase with N steps and the ability to climb either one or two steps at a time,
return the total number of ways to arrive at the top of the staircase.

Ex: Given the following value of N…

N = 2, return 2
1 step + 1 step
2 steps
Ex: Given the following value of N…

N = 3, return 3
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n in {1, 2}:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# Test Cases
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
