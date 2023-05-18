"""
Given an array of integers, nums, return the sum of all uniquely occurring elements.

Ex: Given the following nums…

nums = [1, 3, 5, 5, 2], return 6 (1 + 3 + 2).
Ex: Given the following nums…

nums = [4, 4, 2, 3, 3, 2], return 0.
"""
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = Counter(nums)
        return sum(k for k, v in counts.items() if v == 1)


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfUnique([1, 3, 5, 5, 2]))
    print(solution.sumOfUnique([4, 4, 2, 3, 3, 2]))
