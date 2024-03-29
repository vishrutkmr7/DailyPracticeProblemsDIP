"""
This question is asked by Amazon.
Given an integer array, two players take turns picking the largest number from the ends of the array.
First, player one picks a number (either the left end or right end of the array) followed by player two.
Each time a player picks a particular numbers, it is no longer available to the other player.
This picking continues until all numbers in the array have been chosen. Once all numbers have been picked,
the player with the larger score wins. Return whether or not player one will win. 
Note: You may assume that each player is playing to win (i.e. both players will always choose the
maximum of the two numbers each turn) and that there will always be a winner. 

Ex: Given the following integer array...

nums = [1, 2, 3], return true
Player one takes 3
Player two takes 2
Player one takes 1
3 + 1 > 2 and therefore player one wins
"""


class Solution:
    def willWin(self, nums: list[int]) -> bool:
        dp = [[-1] * len(nums) for _ in nums]

        def get_score(i: int, j: int) -> int:
            if i == j:
                dp[i][j] = 0
                return dp[i][j]
            if i == j - 1:
                dp[i][j] = nums[j] if nums[i] > nums[j] else nums[i]
                return dp[i][j]
            if dp[i][j] != -1:
                return dp[i][j]

            y1 = get_score(i + 1, j - 1)
            y2 = get_score(i + 2, j)
            y3 = get_score(i, j - 2)
            res_y1 = (
                y1 + nums[j] if y1 + nums[j] > y2 + nums[i + 1] else y2 + nums[i + 1]
            )
            res_y2 = (
                y1 + nums[i] if y1 + nums[i] > y3 + nums[j - 1] else y3 + nums[j - 1]
            )

            dp[i][j] = min(res_y1, res_y2)
            return dp[i][j]

        y = get_score(0, len(nums) - 1)
        x = sum(nums) - y

        return 0 if y > x else 1


# Test Cases
print(Solution().willWin([1, 2, 3]))
