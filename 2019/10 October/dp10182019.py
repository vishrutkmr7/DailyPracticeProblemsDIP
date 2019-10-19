#  This problem was recently asked by Uber:

# Given a number of integers, combine them so it would create the largest number.
from itertools import permutations


def largestNum(nums):
    # Fill this in.
    lst = []
    for i in permutations(nums, len(nums)):
        lst.append("".join(map(str, i)))
    return max(lst)


print(largestNum([17, 7, 2, 45, 72]))
# 77245217
