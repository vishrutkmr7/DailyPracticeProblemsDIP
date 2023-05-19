"""
Given an even length string, s, return whether or not the first half of s and the second half of s
contain the same number of vowels.

Ex: Given the following string s…

s = "laptop", return true (there is one vowel in "lap" and one vowel in "top").
Ex: Given the following string s…

s = "computer", return false.
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = set("aeiou")
        first_half = second_half = 0
        for i in range(len(s) // 2):
            if s[i] in vowels:
                first_half += 1
            if s[-i - 1] in vowels:
                second_half += 1
        return first_half == second_half


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.halvesAreAlike("laptop"))  # True
    print(sol.halvesAreAlike("computer"))  # False
