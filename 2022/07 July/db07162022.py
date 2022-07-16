"""
This question is asked by Google.
Given a string of digits, return all possible text messages those digits could send.
Note: The mapping of digits to letters is as follows…

0 -> null
1 -> null
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"
Ex: digits = "23" return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(index, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            for letter in mapping[digits[index]]:
                backtrack(index + 1, curStr + letter)

        if digits:
            backtrack(0, "")

        return result


# Test Cases
print(Solution().letterCombinations("23"))
