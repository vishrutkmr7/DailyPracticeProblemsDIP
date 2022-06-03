"""
This question is asked by Google. Given an array of integers,
return whether or not two numbers sum to a given target, k.
Note: you may not sum a number with itself.

Ex: Given the following...

[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)
"""


def can_sum_to_k(array, k):
    """
    This is a brute force solution.
    """
    if len(array) == 0:
        return False
    if len(array) == 1:
        return array[0] == k
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == k:
                return True
    return False


# Test Cases
print(can_sum_to_k([1, 3, 8, 2], 10))
print(can_sum_to_k([3, 9, 13, 7], 8))
print(can_sum_to_k([4, 2, 6, 5, 2], 4))
