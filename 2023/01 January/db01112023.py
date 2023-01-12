"""
You are given a two-dimensional integer array, grid that represents a map. The grid only consists of zeroes and ones where
zeroes represent water and ones represent land. On the map there’s an island represented as a sequence of contiguous ones
(connected vertically and horizontally) surrounded by zeroes (water). Return the perimeter of the island where each edge
that is touching water represents a size of one.
Note: The island within the map consists of only ones (i.e. there are no “lakes” within the island).

Ex: Given the following grid…

grid = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
], return 4.
Ex: Given the following grid…

grid = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 0]
], return 8.
"""

import itertools


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        for row, col in itertools.product(range(len(grid)), range(len(grid[0]))):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
        return perimeter
