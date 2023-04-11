"""
You are given an integer array that represents the prices of items in a store.
The ith price is given by prices[i]; however, the store is running a special discount.
By buying the ith item, you receive a discount of prices[j] where prices[j] is less
than or equal to prices[i] and j > i. If no such prices[j] exists, you pay for price
for the ith item. Given these prices, return an array that represents the amount you’ll
pay for each respective item considering the special discount.

Ex: Given the following prices…

prices = [3, 2, 2], return [1, 0, 2].
For prices[0] you pay 3 - 1 = 1 dollar.
For prices[1] you pay 2 - 2 = 0 dollars.
For prices[2] you pay 2 dollars.
"""


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n = len(prices)
        dp = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    dp[i] = prices[i] - prices[j]
                    break
            else:
                dp[i] = prices[i]
        return dp


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.finalPrices([3, 2, 2]) == [1, 0, 2]
    assert solution.finalPrices([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert solution.finalPrices([10, 1, 1, 6]) == [9, 0, 1, 6]
    print("All test cases passed!")
