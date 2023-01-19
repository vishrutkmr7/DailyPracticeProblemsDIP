"""
Given an integer, num, convert it to hexadecimal and return the result.

Ex: Given the following num…

num = 15, return "f".
Ex: Given the following num…

num = 46, return "2e".

num = -1, return "ffffffff".
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = 2**32 + num
        hex_map = "0123456789abcdef"
        hex_string = ""
        while num > 0:
            hex_string = hex_map[num % 16] + hex_string
            num //= 16
        return hex_string


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.toHex(15))
    print(solution.toHex(46))
    print(solution.toHex(-1))
