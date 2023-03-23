"""
Given an array of integers, nums, return the “equality index” if it exists and negative one otherwise.
Note: The equality index of the array is the index where the sum of all elements to the left of the
index is equal to the sum of all elements to the right of the index.

Ex: Given the following nums…

nums = [1, 2, 5, 2, 1], return 2 (1 + 2 = 2 + 1)
Ex: Given the following nums…

nums = [3, 1, 9, 2], return -1;
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for index, val in enumerate(nums):
            right_sum -= val
            if left_sum == right_sum:
                return index
            left_sum += val
        return -1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.pivotIndex([1, 2, 5, 2, 1]))
    print(solution.pivotIndex([3, 1, 9, 2]))
