"""
Given a string s and an integer k, return the length of the longest substring in s you can
create that contains a single capital letter. You may apply k operations to s where a single
operation consists of selecting one capital letter and modifying it to be another capital
letter.
Note: s will only contain uppercase alphabetical characters.

Ex: Given the following s and k…

s = "BBAA", k = 2, return 4 (both B's can be changed to A's or both A's can be changed to B's).
"""


from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = defaultdict(int)
        left = 0
        result = 0

        for right, value in enumerate(s):
            hashMap[value] += 1

            while right - left + 1 - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("BBAA", 2))  # 4
