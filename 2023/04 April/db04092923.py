"""
Given an array of integers, nums, and three additional integers, a, b, and c,
return the total number of compatible triplets.
Note: Three integers are said to be a compatible triplet if they are three
individual numbers in nums and
|nums[i] - nums[j]| <= a,
|nums[j] - nums[k]| <= b, and
|nums[i] - nums[k]| <= c.

Ex: Given the following nums…

nums = [1, 2, 3], a = 3, b = 2, c = 5, return 1.
"""


from itertools import combinations


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        C = list(combinations(arr, 3))
        C = [self.checkGood(x, a, b, c) for x in C]
        C = [x for x in C if x is not None]
        return len(C)

    def checkGood(self, tup, a, b, c):
        if (
            abs(tup[0] - tup[1]) <= a
            and abs(tup[0] - tup[2]) <= c
            and abs(tup[2] - tup[1]) <= b
        ):
            return tup
