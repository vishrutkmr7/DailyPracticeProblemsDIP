# This problem was recently asked by Google:

# Given a list of positive numbers, find the largest possible set such that no elements are adjacent numbers of each other.


def maxNonAdjacentSum(nums):
    # Fill this in.
    incl = 0
    excl = 0

    for i in nums:
        new_excl = excl if excl > incl else incl
        incl = excl + i
        excl = new_excl

    return excl if excl > incl else incl


print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# 9
# max sum is 2 (index 0) + 7 (index 3)
