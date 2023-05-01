"""
Given a string, s, return the length of the longest substring that contains every vowel occurring an
even number of times.
Note: You may assume s only contains lowercase alphabetical characters and the vowels you must account
for are a, e, i, o, and u.

Ex: Given the following string s…

s = "aeiouaeioua", return 10 (the last 'a' cannot count).
Ex: Given the following string s…

s = "bbb", return 3 (all vowels occur an even number of times, i.e. zero times each).
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        seen = {0: -1}
        res, cur = 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                cur ^= 1 << vowels[c]
            if cur not in seen:
                seen[cur] = i
            else:
                res = max(res, i - seen[cur])
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.findTheLongestSubstring("aeiouaeioua") == 10
    assert solution.findTheLongestSubstring("bbb") == 3
    print("Success")
