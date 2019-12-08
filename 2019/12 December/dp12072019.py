# This problem was recently asked by Microsoft:

# Given a string, determine if there is a way to arrange the string such that the string is a palindrome.
# If such arrangement exists, return a palindrome (There could be many arrangements). Otherwise return None.
from itertools import permutations
import numpy as np


def checkPalindrome(s):
    rev = s[::-1]
    if s == rev:
        return s


def find_palindrome(s):
    # Fill this in.
    lst = []
    perms = ["".join(p) for p in permutations(s)]
    for i in perms:
        temp = checkPalindrome(i)
        if temp is not None:
            lst.append(i)

    ans = np.array(lst)
    if len(lst) > 0:
        return np.unique(ans)
    else:
        return None


print(find_palindrome("momom"))
# momom
