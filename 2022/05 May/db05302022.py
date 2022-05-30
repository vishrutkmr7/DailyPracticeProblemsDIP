"""
This question is asked by Google.
Given a string, return whether or not it uses capitalization correctly.
A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"lamB", return false
"""


def check_correct_capitalized(string):
    """
    Check if string is capitalized.
    """
    if string in (string.upper(), string.lower()):
        return True
    elif string[0] == string[0].upper() and string[1:] == string[1:].lower():
        return True
    else:
        return False


# Test cases
print(check_correct_capitalized("USA"))
print(check_correct_capitalized("Calvin"))
print(check_correct_capitalized("compUter"))
print(check_correct_capitalized("coding"))
print(check_correct_capitalized("lamB"))
