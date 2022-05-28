"""
This question is asked by Facebook.
Given a string, return whether or not it forms a palindrome
ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
"""
import re


def valid_palindromes(word):
    """Preprocessing."""
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)
    print(word)
    return word == word[::-1]


# Test cases
print(valid_palindromes("level"))
print(valid_palindromes("algorithm"))
print(valid_palindromes("A man, a plan, a canal: Panama."))
