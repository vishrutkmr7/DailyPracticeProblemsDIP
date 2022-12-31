"""
You and your friend are playing a game. In this game, there are piles of pennies in front of you given by an array piles where
piles[i] represents the total number of pennies in the ith pile. In this game, you and your friend take turns removing a pile
from the beginning or end of piles. Once all the pennies are gone, the person who has gathered the most pennies wins.
Given that you move first, return whether or not you can win assuming that you and your friend are both playing optimally.
Note: The total number of piles is even, the total number of pennies is odd, and there is always guaranteed to be a winner.

Ex: Given the following piles…

piles = [2, 1, 4, 4], return true.
Ex: Given the following piles…

piles = [2, 1, 4, 9, 3, 8], return true.
"""


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        """Can win"""
        length = len(piles)

        dp = [[0] * length for _ in range(length)]

        for i in range(length):
            dp[i][i] = piles[i]

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[0][length - 1] > 0


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.stoneGame([2, 1, 4, 4]) is True
    assert solution.stoneGame([2, 1, 4, 9, 3, 8]) is True
    print("All tests passed.")
