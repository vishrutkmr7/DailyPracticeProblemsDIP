"""
Given an array of integers, nums, return an array that contains nums
sorted in ascending order according to their number of one bits.
Note: If two values have the same number of one bits, they should be sorted in ascending order.

Ex: Given the following nums…

nums = [5, 2, 8], return [2, 8, 5] (2 has 1 one bit, 8 has 1 one bit, 5 has 2 one bits).
Ex: Given the following nums…

nums = [4, 5, 5, 1, 3, 9], return [1, 4, 3, 5, 5, 9].
"""


class Solution:
    def sortByBits(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda x: (bin(x).count("1"), x))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortByBits([5, 2, 8]))
    print(solution.sortByBits([4, 5, 5, 1, 3, 9]))
