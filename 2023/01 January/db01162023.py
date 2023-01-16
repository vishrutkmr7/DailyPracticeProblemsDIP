"""
Given an integer array, nums, return an array containing its running sum at every index.

Ex: Given the following nums…

nums = [1, 2, 3], return [1, 3, 6].
Ex: Given the following nums…

nums = [10], return [10].
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.runningSum([1, 2, 3]))
    print(solution.runningSum([10]))
