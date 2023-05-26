"""
Given an integer, N, return its string representation including the necessary commas.

Ex: Given the following N…

N = 200000000, return "200,000,000".
Ex: Given the following N…

N = 5000, return "5,000".
Ex: Given the following N…

N = 100, return "100".
"""


class Solution:
    def addCommas(self, num: int) -> str:
        num = str(num)
        num = num[::-1]
        res = ""
        for i, digit in enumerate(num):
            if i % 3 == 0 and i != 0:
                res += ","
            res += digit
        return res[::-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.addCommas(200000000))  # "200,000,000"
    print(solution.addCommas(5000))  # "5,000"
    print(solution.addCommas(100))  # "100"
