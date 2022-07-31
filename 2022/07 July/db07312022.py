"""
This question is asked by Facebook.
Given an array that represents different coin denominations and an amount of change you need to make,
return the fewest number of coins it takes to make the given amount of change.
Note: If it is not possible to create the amount of change with the coins you’re given, return -1.

Ex: Given the following denominations and amount…

coins = [1,5, 10, 25], amount = 78, return 6
Take three 25 coins and three 1 coins for a total of 6 coins.
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            dp[i] = amount + 1
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != amount + 1 else -1


# Test Cases
print(Solution().coinChange([1, 5, 10, 25], 78))
