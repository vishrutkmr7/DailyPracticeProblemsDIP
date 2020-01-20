#  This problem was recently asked by Microsoft:

# Given two strings which represent non-negative integers, multiply the two numbers and return the product as a string as well.
# You should assume that the numbers may be sufficiently large such that the built-in integer type will not be able to store the input
# (Python does have BigNum, but assume it does not exist).


def multiply(str1, str2):
    # Fill this in.
    return str(int(str1) * int(str2))


print(multiply("11", "13"))
# 143
