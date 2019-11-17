# This problem was recently asked by Google:

# A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k
#  we want to figure out after k random moves by a knight, the probability that the knight will still be on the chessboard.
# Once the knight leaves the board it cannot move again and will be considered off the board.

N = 8

# Direction vector for the Knight
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def inside(x, y):
    return x >= 0 and x < N and y >= 0 and y < N


def is_knight_on_board(x, y, k, cache={}):
    # Fill this in.
    dp1 = [[[0 for i in range(N + 1)] for j in range(N + 1)] for k in range(N + 1)]

    for i in range(N):
        for j in range(N):
            dp1[i][j][0] = 1

    for s in range(1, k + 1):
        for x in range(N):
            for y in range(N):
                prob = 0.0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if inside(nx, ny):
                        prob += dp1[nx][ny][s - 1] / 8.0

                dp1[x][y][s] = prob

    return dp1[x][y][k]


print(is_knight_on_board(0, 0, 1))
# 0.25
