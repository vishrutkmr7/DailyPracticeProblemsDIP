"""
You’ve broken into an art gallery and want to maximize the value of the paintings you steal.
All the paintings you steal you place in your bag which can hold at most W pounds.
Given that the weight and value of the ith painting is given by weights[i] and values[i] respectively,
return the maximum value you can steal.

Ex: Given the following W, weights array and values array…

W = 10, weights = [4, 1, 3], values = [4, 2, 7], return 13.

Ex: Given the following W, weights array and values array…

W = 5, weights = [2, 4, 3], values = [3, 7, 2], return 7.

Ex: Given the following W, weights array and values array…

W = 7, weights = [1, 3, 4], values = [3, 5, 6], return 11.
"""


class Solution:
    def bag(self, W, weights, values):
        dp = [0] * (W + 1)
        dp[0] = 0
        for i in enumerate(weights):
            for j in range(W, -1, -1):
                if j >= weights[i[0]]:
                    dp[j] = max(dp[j], dp[j - weights[i[0]]] + values[i[0]])
        return dp[W]


# Test Cases
print(Solution().bag(10, [4, 1, 3], [4, 2, 7]))
print(Solution().bag(5, [2, 4, 3], [3, 7, 2]))
print(Solution().bag(7, [1, 3, 4], [3, 5, 6]))
