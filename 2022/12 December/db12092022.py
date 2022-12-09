"""
You are playing a game with a friend. In this game you’re given a string s and you and your
friend take turns making moves. A move consists of flipping two consecutive + signs into - signs.
Given a string s, return a list containing all possible states of s after you’ve made the first
move. 

Ex: Given the following string s...

s = “++”, return [“—-“].
Ex: Given the following string s...

s = “++++”, return ["--++","+--+","++--"].
"""


class Solution:
    def generatePossibleNextMoves(self, s: str) -> list[str]:
        return [
            f"{s[:i]}--{s[i + 2:]}"
            for i in range(len(s) - 1)
            if s[i] == s[i + 1] == "+"
        ]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.generatePossibleNextMoves("++"))
    print(solution.generatePossibleNextMoves("++++"))
