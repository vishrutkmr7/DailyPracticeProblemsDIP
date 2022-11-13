"""
Given a string s and a value k, return the length of the longest substring that contains at most
k distinct character.

Ex: Given the following string s and integer k...

s = "abccccd", k = 3, return 6 (“abcccc” is length 6).
Ex: Given the following string s and integer k...

s = "rrr", k = 1, return 3.
"""


from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = Counter()
        left = ans = 0

        for index, value in enumerate(s):
            count[value] += 1

            while len(count) > k:
                if count[s[left]] == 1:
                    del count[s[left]]
                else:
                    count[s[left]] -= 1
                left += 1
            ans = max(ans, index - left + 1)

        return ans


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubstring("abccccd", 3))
    print(solution.longestSubstring("rrr", 1))
