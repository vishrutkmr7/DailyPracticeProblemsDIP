"""
This question is asked by Facebook.
Given a string, reverse the vowels of it.
Note: In this problem y is not considered a vowel.

Ex: Given the following strings s…

s = "computer", return "cemputor"
Ex: Given the following strings s…

s = "The Daily Byte", return "The Dialy Byte"
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)


# Test Cases
s = Solution()
print(s.reverseVowels("computer"))  # returns "cemputor"
print(s.reverseVowels("The Daily Byte"))  # returns "The Dialy Byte"
