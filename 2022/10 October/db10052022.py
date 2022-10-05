"""
Given a 2D array each cells can have one of three values. Zero represents an empty cell,
one represents a healthy person, and two represents a sick person. Each minute that passes,
any healthy person who is adjacent to a sick person becomes sick. Return the total number of minutes
that must elapse until every person is sick.
Note: If it is not possible for each person to become sick, return -1.

Ex: Given the following 2D array grid…

grid = [
    [1,1,1],
    [1,1,0],
    [0,1,2]
], return 4.
[2, 1] becomes sick at minute 1.
[1, 1] becomes sick at minute 2. 
[1, 0] and [0, 1] become sick at minute 3.
[0, 0] and [0, 2] become sick at minute 4.
Ex: Given the following 2D array grid…

grid = [
    [1,1,1],
    [0,0,0],
    [2,0,1]
], return -1.
"""

import itertools


class Solution:
    def __init__(self):
        self.grid = []
        self.m = 0
        self.n = 0
        self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def find_sick(self):
        return [
            (i, j)
            for i, j in itertools.product(range(self.m), range(self.n))
            if self.grid[i][j] == 2
        ]

    def find_healthy(self, sick):
        healthy = []
        for i, j in sick:
            healthy.extend(
                (i + x, j + y)
                for x, y in self.directions
                if (
                    0 <= i + x < self.m
                    and 0 <= j + y < self.n
                    and self.grid[i + x][j + y] == 1
                )
            )
        return healthy

    def solve(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        minutes = 0
        sick = self.find_sick()
        while healthy := self.find_healthy(sick):
            minutes += 1
            for i, j in healthy:
                self.grid[i][j] = 2
            sick = self.find_sick()
        return next((-1 for row in self.grid if 1 in row), minutes)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.solve([[1, 1, 1], [1, 1, 0], [0, 1, 2]]))
    print(solution.solve([[1, 1, 1], [0, 0, 0], [2, 0, 1]]))
