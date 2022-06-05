"""
This question is asked by Facebook.
Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
"""


def valid_anagram(s, t):
    """
    This is a somewhat optimal solution.
    """
    if len(s) != len(t):
        return False
    return sum(s.count(letter) == t.count(letter) for letter in s) == len(s)


# Test Cases
print(valid_anagram("cat", "tac"))
print(valid_anagram("listen", "silent"))
print(valid_anagram("program", "function"))
