"""
Given a string, s, return the length of the longest substring that only contains one unique character.
Note: s is non-empty and it is guaranteed there is a single answer.

Ex: Given the following string s…

s = "aabc", return 2 ("aa" is length 2).
Ex: Given the following string s…

s = "abcabbccabccc", return 3.
"""


class Solution:
    def longestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        longest = 1
        current = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        return max(longest, current)


# Test Cases
if __name__ == "__main__":
    print(Solution().longestSubstring("aabc"))
    print(Solution().longestSubstring("abcabbccabccc"))
