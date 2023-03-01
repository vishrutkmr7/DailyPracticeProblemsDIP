"""
Given an integer, num, that consists of only two digits, sixes and nines, return the largest number you can create
by modifying one digit to be a six or a nine.

Ex: Given the following num…

num = 669, return 969.
Ex: Given the following num…

num = 9969, return 9999.
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


# Test Cases
if __name__ == "__main__":
    num = 669
    print(Solution().maximum69Number(num))
    num = 9969
    print(Solution().maximum69Number(num))
