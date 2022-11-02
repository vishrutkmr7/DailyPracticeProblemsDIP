"""
Given a 2D array of integers with ones representing land and zeroes representing water,
return the number of islands in the grid. Note: an island is one or more ones surrounded by water
connected either vertically or horizontally. Ex: Given the following grid…

11000
11010
11001
return 3.
Ex: Given the following grid…

00100
00010
00001
00001
00010
return 4.
"""


class Solution:
    def num_islands(self, grid):
        """
        :param grid: List[List[int]]
        :return: int
        """
        if not grid:
            return 0
        num_islands = 0
        for i in enumerate(grid):
            for j in range(len(grid[i[0]])):
                if grid[i[0]][j] == 1:
                    num_islands += 1
                    self.dfs(grid, i[0], j)
        return num_islands

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


# Test Cases
s = Solution()
print(
    s.num_islands([[1, 1, 0, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]])
)  # returns 3
print(
    s.num_islands(
        [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
        ]
    )
)  # returns 4
