"""
You are given a certain number of candies and an exchange rate. For every exchange number of
candy wrappers that you trade in, you receive an additional candy. Return the maximum number
of candies that you can eat.
Note: Each candy is wrapped in a candy wrapped.

Ex: Given the following candies and exchange…

candies = 3, exchange = 3, return 4 (each your three candies, exchange 3 wrappers, each
additional candy).
Ex: Given the following candies and exchange…

candies = 3, exchange = 4, return 3.
"""


class Solution:
    def maxCandies(self, candies: int, exchange: int) -> int:
        if candies < exchange:
            return candies
        return candies + self.maxCandies(candies // exchange, exchange)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maxCandies(3, 3) == 4
    assert solution.maxCandies(3, 4) == 3
    print("All test cases passed!")
