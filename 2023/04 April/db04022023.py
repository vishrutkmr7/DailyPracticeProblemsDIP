"""
You are given a two-dimensional matrix containing only ones and zeroes representing a computer network.
Every one in the matrix represents a server and every zero represents an empty space. Two servers within
the network can communicate if they are either in the same row or the same column. Return the total number
of servers that can communicate with at least one other server.

Ex: Given the following matrix…

matrix = [
  [1, 0],
  [1, 0],
], return 2 (both servers are in the same column and can therefore communicate with one another).
Ex: Given the following matrix…

matrix = [
  [1, 0],
  [0, 1],
], return 0.
"""


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        count = 0
        rows_with_servers = [0] * len(grid)
        cols_with_servers = [0] * len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows_with_servers[row] += 1
                    cols_with_servers[col] += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (
                    rows_with_servers[row] > 1 or cols_with_servers[col] > 1
                ):
                    count += 1
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.countServers([[1, 0], [1, 0]]))
    print(solution.countServers([[1, 0], [0, 1]]))
