"""
Given a string, s, return the total number of substrings that only contain one distinct character.

Ex: Given the following string s…

s = "aabbc", return 7. ("a", "aa", "a", "b", "bb", "b", "c").
Ex: Given the following string s…

s = "aaa", return 6.
"""
from collections import Counter


class Solution:
    def countSubstrings(self, s: str) -> int:
        ct = Counter(s)
        return sum(int(cnt * (cnt + 1) / 2) for cnt in ct.values())


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("aabbc"))
    print(sol.countSubstrings("aaa"))
