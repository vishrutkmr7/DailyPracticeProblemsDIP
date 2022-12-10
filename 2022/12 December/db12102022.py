"""
Given an integer, num, return its base seven representation as a string.

Ex: Given the following num...

num = 42, return “60”.
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            return f"-{self.convertToBase7(-num)}"
        ans = ""
        while num:
            ans += str(num % 7)
            num //= 7
        return ans[::-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.convertToBase7(42) == "60"
    assert solution.convertToBase7(100) == "202"
    assert solution.convertToBase7(-7) == "-10"
