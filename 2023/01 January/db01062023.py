"""
Given a binary string s, return the number of contiguous substrings that contains the same number of zeroes and ones.
Note: Each substring’s zeroes and ones must be grouped together.

Ex: Given the following string s…

s = "101", return 2 ("10" and "01").
Ex: Given the following string s…

s = "1011101", return 4 ("10", "01", "10", "01". "101" does not count since the zeroes and ones are not grouped together).
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = list(map(len, s.replace("01", "0 1").replace("10", "1 0").split()))
        return sum(min(a, b) for a, b in zip(s, s[1:]))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.countBinarySubstrings("101"))
    print(solution.countBinarySubstrings("1011101"))
