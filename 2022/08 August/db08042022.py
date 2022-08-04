"""
This question is asked by Google.
Given two strings, s and t, return the length of their longest subsequence.

Ex: Given the following strings s and t…

s = "xyz", t = "xyz". return 3.
Ex: Given the following strings s and t…

s = "abca", t = "acea", return 3.
Ex: Given the following strings s and t…

s = "abc", t = "def", return 0.
"""


class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


# Test Cases
print(Solution().longestCommonSubsequence("xyz", "xyz"))
print(Solution().longestCommonSubsequence("abca", "acea"))
print(Solution().longestCommonSubsequence("abc", "def"))
