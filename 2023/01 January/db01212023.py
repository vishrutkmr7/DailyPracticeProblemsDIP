"""
Given an integer array, nums, return the sum of all subarrays within nums that have an odd length.

Ex: Given the following nums…

nums = [1, 2, 3], return 12 ([1], [2], [3], [1, 2, 3] sum to 12).
Ex: Given the following nums…

nums = [3, 1, 5, 2, 4], return 58.
"""


class Solution:
    def sumOddLengthSubarrays(self, nums: list[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i, len(nums), 2):
                total += sum(nums[i : j + 1])
        return total


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOddLengthSubarrays([1, 2, 3]))
    print(solution.sumOddLengthSubarrays([3, 1, 5, 2, 4]))
