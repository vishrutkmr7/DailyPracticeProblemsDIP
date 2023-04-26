"""
You are given a two-dimensional matrix, grid, containing only ones and zeroes where zeroes represent
land and ones represent water. An “island” is a group of one or more contiguous zeroes connected
four-directionally (i.e. up, down, left and right). A magical island is an island that is completely
surrounded by water on all sides four-directionally. Return the total number of magical islands in
the grid.

Ex: Given the following grid…

grid = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
], return 1.
Ex: Given the following grid…

grid = [
  [1, 1, 1, 0],
  [1, 0, 1, 0],
  [1, 1, 1, 0]
], return 1 (the island in the right-most column is not entirely surrounded by water to
its right for example).
"""


class Solution:
    def numMagicalIslands(self, grid):
        # Time O(m*n) Space O(m*n)
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j]:
                return
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i, v in enumerate(grid):
            for j in range(len(v)):
                if grid[i][j]:
                    dfs(i, j)
                    count += 1
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(solution.numMagicalIslands(grid))  # 1
    grid = [[1, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0]]
    print(solution.numMagicalIslands(grid))  # 1
