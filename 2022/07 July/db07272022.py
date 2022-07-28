"""
This question is asked by Google.
A company is booking flights to send its employees to its two satellite offices A and B.
The cost of sending the ith employee to office A and office B is given by prices[i][0]
and prices[i][1] respectively. Given that half the employees must be sent to office A
and half the employees must be sent to office B, return the minimum cost the company must pay
for all their employees’ flights.

Ex: Give the following prices…

prices = [[40,30],[300,200],[50,50],[30,60]], return 310
Fly the first person to office B.
Fly the second person to office B.
Fly the third person to office A.
Fly the fourth person to office A.
"""


class Solution:
    def minCost(self, prices: list[list[int]]) -> int:
        prices.sort(key=lambda x: x[1] - x[0])
        return sum(
            cost[1] if i < len(prices) / 2 else cost[0] for i, cost in enumerate(prices)
        )


# Test Cases
print(Solution().minCost([[40, 30], [300, 200], [50, 50], [30, 60]]))
