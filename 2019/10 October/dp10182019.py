#  This problem was recently asked by Uber:

# Given a number of integers, combine them so it would create the largest number.
from itertools import permutations


def largestNum(nums):
    # Fill this in.
    lst = ["".join(map(str, i)) for i in permutations(nums, len(nums))]
    return max(lst)


print(largestNum([17, 7, 2, 45, 72]))
# 77245217
