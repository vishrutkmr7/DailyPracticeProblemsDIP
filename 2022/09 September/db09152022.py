"""
You are given two-dimensional matrix that represents a plot of land. Within the matrix there exist two values:
ones which represent land and zeroes which represent water within a pond. Given that parts of a pond can be
connected both horizontally and vertically (but not diagonally), return the largest pond size.
Note: You may assume that each zero within a given pond contributes a value of one to the total size of the pond.

Ex: Given the following plot of land…

land = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
], return 1.
Ex: Given the following plot of land…

land = [
    [1,0,1],
    [0,0,0],
    [1,0,1]
], return 5.
"""


class Solution:
    def largestPond(self, land: list[list[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]) or land[i][j] != 0:
                return 0

            land[i][j] = -1
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        return max(dfs(i, j) for i in range(len(land)) for j in range(len(land[0])))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.largestPond(
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1],
            ]
        )
    )
    print(
        solution.largestPond(
            [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1],
            ]
        )
    )
