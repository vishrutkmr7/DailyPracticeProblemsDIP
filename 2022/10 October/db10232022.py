"""
Given an integer n, return whether or not it is a “magical” number.
A magical number is an integer such that when you repeatedly replace the number with the
sum of the squares of its digits its eventually becomes one.

Ex: Given the following integer n…

n = 19, return true.
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1.
Ex: Given the following integer n…

n = 22, return false
"""


class Solution:
    def isMagical(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isMagical(19))
    print(solution.isMagical(22))
