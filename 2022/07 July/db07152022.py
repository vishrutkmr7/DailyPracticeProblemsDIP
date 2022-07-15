"""
This question is asked by Amazon.
Given a string s consisting of only letters and digits,
where we are allowed to transform any letter to uppercase or lowercase,
return a list containing all possible permutations of the string.

Ex: Given the following string…

S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]
"""


import itertools


def get_permutations(s):
    return list(set(map("".join, itertools.product(*zip(s.upper(), s.lower())))))


# Test Cases
print(get_permutations("c7w2"))
