"""This question is asked by Amazon.
Given a 2D board that represents a word search puzzle and a string word,
return whether or the given word can be formed in the puzzle by only connecting cells horizontally and vertically.

Ex: Given the following board and words…

board =
[
  ['C','A','T','F'],
  ['B','G','E','S'],
  ['I','T','A','E']
]
word = "CAT", return true
word = "TEA", return true
word = "SEAT", return true
word = "BAT", return false
"""


class Solution:
    def wordSearch(self, board, word):
        if not board or not word:
            return False
        if len(board) == 0 or len(board[0]) == 0:
            return False
        if len(word) == 0:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if (
            i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[0])
            or board[i][j] != word[0]
        ):
            return False
        temp = board[i][j]
        board[i][j] = "#"
        res = (
            self.dfs(board, i + 1, j, word[1:])
            or self.dfs(board, i - 1, j, word[1:])
            or self.dfs(board, i, j + 1, word[1:])
            or self.dfs(board, i, j - 1, word[1:])
        )
        board[i][j] = temp
        return res


# Test Cases
board = [
    ["C", "A", "T", "F"],
    ["B", "G", "E", "S"],
    ["I", "T", "A", "E"],
]
word = "CAT"
print(Solution().wordSearch(board, word))
word = "TEA"
print(Solution().wordSearch(board, word))
word = "SEAT"
print(Solution().wordSearch(board, word))
word = "BAT"
print(Solution().wordSearch(board, word))
