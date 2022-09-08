"""
This question is asked by Apple.
Given a 32 bit signed integer, reverse it and return the result.
Note: You may assume that the reversed integer will always fit within the bounds of the integer data type.

Ex: Given the following integer num…

num = 550, return 55
Ex: Given the following integer num…

num = -37, return -73
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -int(str(-x)[::-1]) if -int(str(-x)[::-1]) >= -(2**31) else 0
        return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2**31 - 1 else 0


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(550))
    print(solution.reverse(-37))
