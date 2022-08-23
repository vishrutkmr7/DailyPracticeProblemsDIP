"""
This question is asked by Google.
Given two strings s and t return whether or not s is a subsequence of t.
Note: You may assume both s and t only consist of lowercase characters and both have a length of at least one.

Ex: Given the following strings s and t…

s = "abc", t = "aabbcc", return true.
Ex: Given the following strings s and t…

s = "cpu", t = "computer", return true.
Ex: Given the following strings s and t…

s = "xyz", t = "axbyc", return false.
"""


class Solution:
    def is_subsequence(self, s, t):
        """
        :param s: string
        :param t: string
        :return: boolean
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        if s[0] == t[0]:
            return self.is_subsequence(s[1:], t[1:])
        return self.is_subsequence(s, t[1:])


# Test Cases
s = Solution()
print(s.is_subsequence("abc", "aabbcc"))  # returns true
print(s.is_subsequence("cpu", "computer"))  # returns true
print(s.is_subsequence("xyz", "axbyc"))  # returns false
