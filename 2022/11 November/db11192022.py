"""
Given an array integers, prices, where each values represents the price of a stock on the ith day,
return the maximum profit you can make making a single transaction (i.e. one buy and one sell)
of one share of stock.

Ex: Given the following prices...

prices = [8, 9, 2, 3, 5, 2, 4], return 3.
Ex: Given the following prices...

prices = [10, 8, 3, 1], return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([8, 9, 2, 3, 5, 2, 4]))
    print(solution.maxProfit([10, 8, 3, 1]))
