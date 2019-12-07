# This problem was recently asked by Microsoft:

# A maze is a matrix where each cell can either be a 0 or 1. A 0 represents that the cell is empty, and a 1 represents a wall
# that cannot be walked through. You can also only travel either right or down.

# Given a nxm matrix, find the number of ways someone can go from the top left corner to the bottom right corner.
# You can assume the two corners will always be 0.

# Maze dimensions
R = 3
C = 3


def paths_through_maze(maze):
    # Fill this in.
    if maze[0][0] == 1:
        return

    for i in range(R):
        if maze[i][0] == 0:
            maze[i][0] = -1
        else:
            break

    for i in range(1, C, 1):
        if maze[0][i] == 0:
            maze[0][i] = -1
        else:
            break

    for i in range(1, R, 1):
        for j in range(1, C, 1):
            if maze[i][j] == 1:
                continue  # Blockage

            if maze[i - 1][j] < 0:
                maze[i][j] = maze[i][j] + maze[i - 1][j]

            if maze[i][j - 1] < 0:
                maze[i][j] = maze[i][j] + maze[i][j - 1]

    # If the final cell is blocked
    if maze[R - 1][C - 1] < 0:
        return abs(maze[R - 1][C - 1])  # Count was -vely increased
    else:
        return 0


print(paths_through_maze([[0, 1, 0], [0, 0, 1], [0, 0, 0]]))
# 2
