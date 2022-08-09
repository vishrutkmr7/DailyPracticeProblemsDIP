"""
This question is asked by Apple.
You are tasked with painting a row of houses in your neighborhood such that
each house is painted either red, blue, or green. The cost of painting the ith house
red, blue or green, is given by costs[i][0], costs[i][1], and costs[i][2] respectively.
Given that you are required to paint each house and no two adjacent houses may be the same color,
return the minimum cost to paint all the houses.

Ex: Given the following costs array…

costs = [[1, 3, 5],[2, 4, 6],[5, 4, 3]], return 8.
Paint the first house red, paint the second house blue, and paint the third house green.
"""


class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        for i in range(n):
            for j in range(3):
                if i == 0:
                    dp[i][j] = costs[i][j]
                else:
                    dp[i][j] = (
                        min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
                        + costs[i][j]
                    )

        return min(dp[-1])


# Test Cases
costs = [[1, 3, 5], [2, 4, 6], [5, 4, 3]]
print(Solution().minCost(costs))
