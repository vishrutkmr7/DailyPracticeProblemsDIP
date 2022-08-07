"""
This question is asked by Amazon.
Given a string s and a list of words representing a dictionary,
return whether or not the entirety of s can be segmented into dictionary words.
Note: You may assume all characters in s and the dictionary are lowercase.

Ex: Given the following string s and dictionary…

s = "thedailybyte", dictionary = ["the", "daily", "byte"], return true.

Ex: Given the following string s and dictionary…

s = "pizzaplanet", dictionary = ["plane", "pizza"], return false.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        m, n = len(s), len(wordDict)
        dp = [False] * (m + 1)
        dp[0] = True
        for i in range(1, m + 1):
            for j in range(n):
                if (
                    dp[i - len(wordDict[j])]
                    and s[i - len(wordDict[j]) : i] == wordDict[j]
                ):
                    dp[i] = True
                    break
        return dp[m]


# Test Cases
s = "thedailybyte"
wordDict = ["the", "daily", "byte"]
print(Solution().wordBreak(s, wordDict))

s = "pizzaplanet"
wordDict = ["plane", "pizza"]
print(Solution().wordBreak(s, wordDict))
