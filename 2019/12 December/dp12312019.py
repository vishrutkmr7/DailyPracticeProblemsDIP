# This problem was recently asked by Facebook:

# A Sudoku board is a 9x9 grid, where each row, column and each 3x3 subbox contains the number from 1-9. Here's an example of a Sudoku board.
# -------------
# |534|678|912|
# |672|195|348|
# |198|342|567|
# |------------
# |859|761|423|
# |426|853|791|
# |713|924|856|
# |------------
# |961|537|284|
# |287|419|635|
# |345|286|179|
# |------------

# Given a 9x9 board, determine if it is a valid Sudoku board. The board may be partially filled,
# where an empty cell will be represented by the space character ' '.


def notInRow(arr, row):

    st = set()

    for i in range(0, 9):
        if arr[row][i] in st:
            return False

        if arr[row][i] != " ":
            st.add(arr[row][i])

    return True


def notInCol(arr, col):

    st = set()

    for i in range(0, 9):
        if arr[i][col] in st:
            return False

        if arr[i][col] != " ":
            st.add(arr[i][col])

    return True


def notInBox(arr, startRow, startCol):

    st = set()

    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]

            if curr in st:
                return False

            if curr != " ":
                st.add(curr)

    return True


def isValid(arr, row, col):

    return (
        notInRow(arr, row)
        and notInCol(arr, col)
        and notInBox(arr, row - row % 3, col - col % 3)
    )


def validate_sudoku(board):
    # Fill this in.
    n = 9
    for i in range(0, n):
        for j in range(0, n):

            if not isValid(board, i, j):
                return False

    return True


board = [
    [5, " ", 4, 6, 7, 8, 9, 1, 2],
    [6, " ", 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

print(validate_sudoku(board))
# True
