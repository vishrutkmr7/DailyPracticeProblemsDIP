"""
This question is asked by Google.
Given two strings s and t, return the minimum number of operations needed to convert
s into t where a single operation consists of inserting a character, deleting a character, or replacing a character.

Ex: Given the following strings s and t…

s = "cat", t = "bat", return 1.

Ex: Given the following strings s and t…

s = "beach", t = "batch", return 2.
Delete the 'e' in "beach" and add a 't' to the resulting "bach".
"""


class Solution:
    def min_operations(self, s, t):
        """
        :param s: string
        :param t: string
        :return: int
        """
        if s == t:
            return 0
        if len(s) > len(t):
            return self.min_operations(t, s)
        if len(s) == 0:
            return len(t)
        if s[0] == t[0]:
            return self.min_operations(s[1:], t[1:])
        return 1 + min(self.min_operations(s, t[1:]), self.min_operations(s[1:], t))


# Test Cases
s = "cat"
t = "bat"
print(Solution().min_operations(s, t))

s = "beach"
t = "batch"
print(Solution().min_operations(s, t))
