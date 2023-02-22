"""
Given an integer array, nums, return true if all values within nums occur a unique number of times. Otherwise, return false.

Ex: Given the following nums…

nums = [1, 3, 3, 2, 2, 2], return true (1 appears once, 3 appears twice, two appears 3 times).
Ex: Given the following nums…

nums = [4, 10], return false (both 4 and 10 occur once).
"""
from collections import Counter


class Solution:
    def uniqueOccurrences(self, nums: list[int]) -> bool:
        count = Counter(nums)
        return len(count.values()) == len(set(count.values()))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniqueOccurrences([1, 3, 3, 2, 2, 2]))
    print(solution.uniqueOccurrences([4, 10]))
