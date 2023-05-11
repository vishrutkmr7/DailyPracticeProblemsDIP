"""
Given an array of integers, nums, and an integer, k, return the least number of unique numbers
left in nums after removing k elements.
Note: At least one integer will exist in nums and k will always be between zero and nums.length.

Ex: Given the following nums and k…

nums = [1, 4, 3, 3], k = 2, return 1 (remove 1 and 4 and only one unique integer is left which is 3).
"""


from collections import Counter
from heapq import heapify, heappop


class Solution:
    def findLeastNumOfUniqueInts(self, nums: list[int], k: int) -> int:
        hp = list(Counter(nums).values())
        heapify(hp)
        while k > 0:
            k -= heappop(hp)
        return len(hp) + (k < 0)


# Test Cases
solution = Solution()
assert solution.findLeastNumOfUniqueInts([1, 4, 3, 3], 2) == 1
