# This problem was recently asked by Facebook:

# You are given an array of integers. Return the smallest positive integer that is not present in the array.\
# The array may contain duplicate entries.

# Your solution should run in linear time and use constant space


def first_missing_positive(nums):
    # Fill this in.
    m = max(nums)
    if m < 1:
        return 0
    if len(nums) == 1:
        return 2 if nums[0] == 1 else 1

    l = [0] * m
    for i in range(len(nums)):
        if nums[i] > 0:
            if l[nums[i] - 1] != 1:
                l[nums[i] - 1] = 1

    for i in range(len(l)):
        if l[i] == 0:
            return i + 1

    return i + 2


print(first_missing_positive([3, 4, -1, 1]))
# 2
