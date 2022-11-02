"""
Given a string s, return the length of the longest substring that contains only unique characters.

Ex: Given the following string s…

s = "ababbc", return 2.
Ex: Given the following string s…

s = "abcdssa", return 5.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        start = 0
        maxL = 0
        for ch in s:
            if ch not in curr:
                curr.add(ch)
            else:
                maxL = max(maxL, len(curr))
                while s[start] != ch:
                    curr.remove(s[start])
                    start += 1
                start += 1
        return max(maxL, len(curr))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("ababbc"))
    print(solution.lengthOfLongestSubstring("abcdssa"))
