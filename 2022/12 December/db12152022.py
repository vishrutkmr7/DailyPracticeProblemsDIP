"""
Given a string, s, which consists of only lowercase alphabetical characters, return the length of
the longest palindrome you can form using its letters.

Ex: Given the following s...

s = “aa”, return 2.
Ex: Given the following s...

s = “abbcaadabac”, return 9.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        odd_count = sum(value % 2 == 1 for value in char_count.values())
        return len(s) if odd_count == 0 else len(s) - odd_count + 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("aa"))
    print(solution.longestPalindrome("abbcaadabac"))
