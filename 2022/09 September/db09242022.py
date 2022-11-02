"""
Given a string s, return the length of the longest substring containing at most two distinct characters.
Note: You may assume that s only contains lowercase alphabetical characters.

Ex: Given the following value of s…

s = "aba", return 3.
Ex: Given the following value of s…

s = "abca", return 2.
"""


class Solution:
    def longestSubstring(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        left = 0
        max_length = 2
        char_count = {}
        for right in enumerate(s):
            char_count[s[right[0]]] = char_count.get(s[right[0]], 0) + 1
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_length = max(max_length, right[0] - left + 1)
        return max_length


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubstring("aba"))
    print(solution.longestSubstring("abca"))
