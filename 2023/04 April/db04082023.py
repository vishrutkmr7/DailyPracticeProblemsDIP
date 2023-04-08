"""
Given a list of moves in a game of tic tac toe, return that state of the game.
If player A (the first player to move with X characters) wins, return ”A”.
If player B (the second player to move with O characters) wins, return ”B”.
Otherwise, if it’s a draw, return ”Draw” and if the game hasn’t finished, return ”Pending”.

Ex: Given the following moves…

moves = [[0,0],[1,0],[1,1],[2,0],[2,2]], return "A" (player A won with three Xs
being connected along the diagonal).
"""


class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        board = [[0] * 3 for _ in range(3)]
        for i, (x, y) in enumerate(moves):
            board[x][y] = "A" if i % 2 == 0 else "B"
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != 0:
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != 0:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != 0:
            return board[0][2]
        return "Draw" if len(moves) == 9 else "Pending"


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.tictactoe([[0, 0], [1, 0], [1, 1], [2, 0], [2, 2]]))
