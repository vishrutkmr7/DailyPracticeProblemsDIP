#  This problem was recently asked by Facebook:

# You are given an array of integers. Return all the permutations of this array.
from itertools import permutations


def permute(nums):
    # Fill this in.
    ans = []
    for i in permutations(nums, len(nums)):
        ans.append(list(i))

    return ans


print(permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
