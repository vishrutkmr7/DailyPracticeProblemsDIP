"""
Given two non-negative numbers, num1 and num2 represented as strings, sum the integers
together and return the result as a string.

Ex: Given the following values for num1 and num2...

num1 = “2”, num2 = “5”, return “7”.
Ex: Given the following values for num1 and num2...

num1 = “7”, num2 = “95”, return “102”.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.addStrings("2", "5"))
    print(solution.addStrings("7", "95"))
