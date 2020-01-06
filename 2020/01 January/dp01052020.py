# This problem was recently asked by Microsoft:

# N-Queens is the problem where you find a way to put n queens on a nxn chess board without them being able to attack each other.
# Given an integer n, return 1 possible solution by returning all the queen's position.


def printSolution(board, N):
    resArr = []
    for i in range(0, N):
        for j in range(0, N):
            if board[i][j] == 1:
                resArr.append((i, j))

    return resArr


def isSafe(board, row, col, N):

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, N):
    if col >= N:
        return True
    for i in range(N):

        if isSafe(board, i, col, N):
            board[i][col] = 1

            if solveNQUtil(board, col + 1, N) == True:
                return True

            board[i][col] = 0

    return False


def n_queens(n):
    # Fill this in.
    # n x n board
    board = [[0 for x in range(n)] for y in range(n)]

    if solveNQUtil(board, 0, n) == False:
        return "Solution does not exist"

    return printSolution(board, n)


print(n_queens(5))
# There can be many answers
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .
