# This problem was recently asked by Facebook:

# Given a list of unique numbers, generate all possible subsets without duplicates. This includes the empty set as well.


def generateAllSubsets(nums):
    # Fill this in.
    x = len(nums)
    res = []
    for i in range(1 << x):
        res.append([nums[j] for j in range(x) if (i & (1 << j))])

    return res


print(generateAllSubsets([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
