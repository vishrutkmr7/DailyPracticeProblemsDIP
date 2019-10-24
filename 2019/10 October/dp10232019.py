# This problem was recently asked by Amazon:

# You are given an array of integers, and an integer K. Return the subarray which sums to K.
# You can assume that a solution will always exist.

import itertools as it
import numpy as np


def find_continuous_k(arr, k):
    # Fill this in.
    maxsize = np.argwhere(np.cumsum(sorted(arr)) > k)[0][0]
    subsets = []
    for size in range(1, maxsize + 1):
        subsets.extend([t for t in it.combinations(arr, size) if sum(t) == k])

    return list(subsets[0])


print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
