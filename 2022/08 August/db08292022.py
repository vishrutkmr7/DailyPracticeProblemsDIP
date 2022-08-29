"""
This question is asked by Google.
Given an NxM matrix, grid, where each cell in the matrix represents the cost of stepping on the current cell,
return the minimum cost to traverse from the top-left hand corner of the matrix to the bottom-right hand corner.
Note: You may only move down or right while traversing the grid.

Ex: Given the following grid…

grid = [
    [1,1,3],
    [2,3,1],
    [4,6,1]
], return 7.
The path that minimizes our cost is 1->1->3->1->1 which sums to 7.
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # create 2D array to store sub-problem results
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])

        return dp[m - 1][n - 1]
