"""
This question is asked by Amazon.
Given a 2D matrix that represents a gold mine, where each cell’s value represents an amount of gold,
return the maximum amount of gold you can collect given the following rules:

1. You may start and stop collecting gold from any position
2. You can never visit a cell that contains 0 gold
3. You cannot visit the same cell more than once
4. From the current cell, you may walk one cell to the left, right, up, or down

Ex: Given the following gold mine…

goldMine = [
    [0,2,0],
    [8,6,3],
    [0,9,0]
],
return 23 (start at 9 and then move to 6 and 8 respectively)
"""


class Solution:
    def getMaximumGold(self, grid):
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0
                or r >= row
                or c < 0
                or c >= col
                or grid[r][c] == 0
                or grid[r][c] == "#"
            ):
                return 0
            temp = grid[r][c]
            grid[r][c] = "#"
            point = max(
                dfs(r + 1, c) + temp,
                dfs(r - 1, c) + temp,
                dfs(r, c + 1) + temp,
                dfs(r, c - 1) + temp,
            )

            grid[r][c] = temp

            return point

        point = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                point = max(dfs(r, c), point)

        return point


# Test Cases
goldMine = [[0, 2, 0], [8, 6, 3], [0, 9, 0]]
print(Solution().getMaximumGold(goldMine))
