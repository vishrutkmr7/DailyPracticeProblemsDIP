# This problem was recently asked by LinkedIn:

# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present in the grid. The definition of an island is as follows:
# 1.) Must be surrounded by water blocks.
# 2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.


class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    def isSafe(self, i, j, visited):
        return (
            i >= 0
            and i < self.ROW
            and j >= 0
            and j < self.COL
            and not visited[i][j]
            and self.graph[i][j]
        )

    def DFS(self, i, j, visited):
        # For the 8 neighbors of a cell
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    def numIslands(self):
        # Fill this in.
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.DFS(i, j, visited)
                    count += 1

        return count


grid = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0]]
row = len(grid)
col = len(grid[0])
g = Graph(row, col, grid)
print(g.numIslands())
# 3
