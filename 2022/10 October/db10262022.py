"""
Given a 2D array grid, where zeroes represent water and ones represent land,
return the size of the largest island.
Note: An island is one or more cells in grid containing a value of one that
may be connected vertically or horizontally. Each cell in an island contributes
a value of one to the current island’s size.

Ex: Given the following grid...

grid = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
], return 4.
"""


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return 0

        max_area = 0
        for index, _ in enumerate(grid):
            for j in range(len(grid[0])):
                if grid[index][j] == 1:
                    max_area = max(max_area, dfs(index, j))
        return max_area


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestIsland([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
