"""
You are given the list of prices of a particular stock. Each element in the array represents
the price of the stock at a given second throughout the current day. Return the maximum profit
you can make trading this stock.
Note: You may only ever buy and sell a single share of the stock, but you may make multiple
transactions (i.e. buys and sells).
Ex: Given the following prices...

prices = [8, 3, 2, 4, 6, 4, 5], return 5.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return (
            sum(
                prices[i] - prices[i - 1]
                for i in range(1, len(prices))
                if prices[i] > prices[i - 1]
            )
            if prices
            else 0
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([8, 3, 2, 4, 6, 4, 5]))
