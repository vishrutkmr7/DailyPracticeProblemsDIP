"""
Given a string, s, that contains a valid set of parentheses, return the maximum depth of the
parentheses seen at any point of the string.
Note: For example, “abc”, “()”, and “(()), have depths of zero, one, and two respectively.

Ex: Give the following string s…

s = "The(Daily)Byte", return 1.
Ex: Give the following string s…

s = ""The(Daily)Byte((Dot)Dev)"", return 2.
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        currentDepth = 0
        for char in s:
            if char == "(":
                currentDepth += 1
            elif char == ")":
                currentDepth -= 1
            maxDepth = max(maxDepth, currentDepth)
        return maxDepth


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDepth("The(Daily)Byte"))
    print(solution.maxDepth("The(Daily)Byte((Dot)Dev)"))
