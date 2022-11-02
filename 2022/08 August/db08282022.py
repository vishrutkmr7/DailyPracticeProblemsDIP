"""
This question is asked by Amazon.
Given a string s remove all the vowels it contains and return the resulting string. 
Note: In this problem y is not considered a vowel. 

Ex: Given the following string s…

s = "aeiou", return ""
Ex: Given the following string s…

s = "byte", return "byt"
Ex: Given the following string s…

s = "xyz", return "xyz"
"""


class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        return "".join([c for c in s if c not in vowels])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.removeVowels("aeiou") == ""
    assert solution.removeVowels("byte") == "byt"
    assert solution.removeVowels("xyz") == "xyz"
    print("All tests passed.")
