"""
Given two strings s and t, return the index of the first occurrence of t within s if it exists; otherwise, return -1.

Ex: Given the following strings s and t…

s = "abc", t = "a", return 0.
Ex: Given the following strings s and t…

s = "abc", t = "abcd", return -1.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return -1 if needle not in haystack else haystack.index(needle)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.strStr("abc", "a") == 0
    assert solution.strStr("abc", "abcd") == -1
    print("All tests passed.")
