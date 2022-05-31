"""
This question is asked by Apple.
Given two binary strings (strings containing only 1s and 0s) return their sum
(also as a binary string). 
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
"""


def binary_addition(a, b):
    """
    The binary strings will be padded with 0s to be the same length.
    """
    sum_binary = bin(int(a, 2) + int(b, 2))
    return sum_binary[2:]


# Test cases
print(binary_addition("100", "1"))
print(binary_addition("11", "1"))
print(binary_addition("1", "0"))
