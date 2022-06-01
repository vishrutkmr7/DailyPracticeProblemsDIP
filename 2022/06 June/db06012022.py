"""
This question is asked by Microsoft.
Given an array of strings, return the longest common prefix that is shared amongst all strings. 
Note: you may assume all strings only contain lowercase alphabetical characters. 

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted", "spotify"], return "spot"
"""


def longest_common_prefix(arr):
    """
    This is a brute force solution.
    """
    if len(arr) == 0:
        return ""
    if len(arr) == 1:
        return arr[0]
    prefix = ""
    for i in range(len(arr[0])):
        for j in range(1, len(arr)):
            if i >= len(arr[j]) or arr[j][i] != arr[0][i]:
                return prefix
        prefix += arr[0][i]
    return prefix


# Test cases
print(longest_common_prefix(["colorado", "color", "cold"]))
print(longest_common_prefix(["a", "b", "c"]))
print(longest_common_prefix(["spot", "spotty", "spotted", "spotify"]))
