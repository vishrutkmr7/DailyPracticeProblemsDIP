"""
Given a string, s, return whether or not some permutation of s could form a palindrome.

Ex: Given the following string s…

s = "aeae", return true ("aeea" or "eaae").
Ex: Given the following string s…

s = "computer", return false.
"""


from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(v % 2 for v in Counter(s).values()) < 2


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.canPermutePalindrome("aeae"))
    print(solution.canPermutePalindrome("computer"))
