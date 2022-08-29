"""
Given a 2D array containing only the following values: -1, 0, 1 where -1 represents an obstacle,
0 represents a rabbit hole, and 1 represents a rabbit, update every cell containing a rabbit with the
distance to its closest rabbit hole.

Note: multiple rabbit may occupy a single rabbit hole and you may assume every rabbit can reach a rabbit hole.
A rabbit can only move up, down, left, or right in a single move. Ex: Given the following grid…

-1  0  1
 1  1 -1
 1  1  0
your grid should look like the following after running the function...
-1  0  1
 2  1 -1
 2  1  0
Ex: Given the following grid…

 1  1  1
 1 -1 -1
 1  1  0
your grid should look like the following after running the function...
4  5  6
3 -1 -1
2  1  0
"""


import itertools


class Solution:
    def updateMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        if not grid:
            return grid
        m, n = len(grid), len(grid[0])
        q = []
        for i, j in itertools.product(range(m), range(n)):
            if grid[i][j] == 0:
                q.append((i, j))
            else:
                grid[i][j] = float("inf")
        while q:
            i, j = q.pop(0)
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j] + 1:
                    grid[x][y] = grid[i][j] + 1
                    q.append((x, y))
        return grid


# Test Cases
sol = Solution()
print(sol.updateMatrix([[-1, 0, 1], [1, 1, -1], [1, 1, 0]]))
print(sol.updateMatrix([[1, 1, 1], [1, -1, -1], [1, 1, 0]]))
