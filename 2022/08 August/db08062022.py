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


from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        @cache
        def dp(i, j):
            if i == 0:
                return j
            if j == 0:
                return i

            l1, l2 = word1[i - 1], word2[j - 1]
            if l1 != l2:
                return 1 + min(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j - 1))
            return dp(i - 1, j - 1)

        return dp(m, n)


# Test Cases
s = "cat"
t = "bat"
print(Solution().minDistance(s, t))

s = "beach"
t = "batch"
print(Solution().minDistance(s, t))
