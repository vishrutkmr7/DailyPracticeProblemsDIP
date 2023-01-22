"""
You are given an integer array, nums, that contains 2N integers. Return the maximum sum you can create by pairing integers
together and summing the minimum values in each of the pairs.

Ex: Given the following nums…

nums = [1, 3, 2, 4], return 4 (min(1, 2) + min(3, 4) = 4).
Ex: Given the following nums…

nums = [2, 4, 2, 8, 4, 3], return 9.
"""


class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[::2])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.arrayPairSum([1, 3, 2, 4]))
    print(solution.arrayPairSum([2, 4, 2, 8, 4, 3]))
