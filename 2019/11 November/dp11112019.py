# Twitter: Given an integer, check if that integer is a palindrome.
# For this problem do not convert the integer to a string to check if it is a palindrome.

import math


def is_palindrome(n):
    # Fill this in.
    divisor = 1
    while n / divisor >= 10:
        divisor *= 10

    while n != 0:

        leading = n // divisor
        trailing = n % 10
        if leading != trailing:
            return False
        n = (n % divisor) // 10
        divisor = divisor / 100

    return True


print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
