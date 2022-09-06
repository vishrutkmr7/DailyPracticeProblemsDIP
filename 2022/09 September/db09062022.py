"""
Given a list of words, return all the words that require only a single row of a keyboard to type.
Note: You may assume that all words only contain lowercase alphabetical characters.

Ex: Given the following list of words…

words = ["two", "dad", "cat"], return ["two", "dad"].
Ex: Given the following list of words…

words = ["ufo", "xzy", "byte"], return [].
"""


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        return [
            word
            for word in words
            if set(word.lower()).issubset(row1)
            or set(word.lower()).issubset(row2)
            or set(word.lower()).issubset(row3)
        ]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findWords(["two", "dad", "cat"]))
    print(solution.findWords(["ufo", "xzy", "byte"]))
