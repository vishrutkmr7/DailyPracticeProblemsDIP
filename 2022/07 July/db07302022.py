"""
This question is asked by Apple.
Given a staircase where the ith step has a non-negative cost associated with it given by cost[i],
return the minimum cost of climbing to the top of the staircase.
You may climb one or two steps at a time and you may start climbing from either the first or second step. 

Ex: Given the following cost array…

cost = [5, 10, 20], return 10.

Ex: Given the following cost array…

cost = [1, 5, 10, 3, 7, 2], return 10.
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])


# Test Cases
print(Solution().minCostClimbingStairs([5, 10, 20]))
print(Solution().minCostClimbingStairs([1, 5, 10, 3, 7, 2]))
