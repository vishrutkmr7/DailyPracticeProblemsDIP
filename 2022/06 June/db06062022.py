"""
This question is asked by Microsoft.
Given a string, return the index of its first unique character. 
If a unique character does not exist, return -1. 

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""


def first_unique_character(string):
    """
    This is a somewhat optimal solution.
    """
    if len(string) == 0:
        return -1
    return next((i for i in range(len(string)) if string.count(string[i]) == 1), -1)


# Test Cases
print(first_unique_character("abcabd"))
print(first_unique_character("thedailybyte"))
print(first_unique_character("developer"))
