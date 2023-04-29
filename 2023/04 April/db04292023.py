"""
You are given a two-dimensional matrix, grid, that only contains zeroes and ones. Zeroes represent
water and ones represent land. Return the furthest distance any cell with water is from any cell
with land.
Note: One cell represents a unit distance of one and you may only travel four-directionally
from any given cell (i.e. up, down, left, and right). If no land exists within grid, return -1.

Ex: Given the following grid…

grid = [
  [0, 0, 1],
  [0, 0, 0],
  [0, 0, 0]
], return 4 (cell (0, 2) is 4 units away from cell (2, 0)).
Ex: Given the following grid…

grid = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
], return 2.
"""
from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) in [0, m * n]:
            return -1
        level = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i, new_j = i + x, j + y
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 0:
                        grid[new_i][new_j] = 1
                        q.append((new_i, new_j))
            level += 1
        return level - 1


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDistance([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))  # 4
    print(sol.maxDistance([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
