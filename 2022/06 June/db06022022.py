"""
This question is asked by Facebook.
Given a stringing and the ability to delete at most one character,
return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
"""


def check_palindrome(word):
    """
    Used from prev. files
    """
    return word == word[::-1]


def can_form_palindrome(string):
    """
    This is a brute force solution.
    """
    if len(string) == 0:
        return True
    if len(string) == 1:
        return True
    # Removing the mids
    mid = len(string) // 2
    mod = (len(string) + 1) % 2
    return check_palindrome(string[: mid - mod] + string[mid + 1 :])


# Test cases
print(can_form_palindrome("abcba"))
print(can_form_palindrome("foobof"))
print(can_form_palindrome("abccab"))
