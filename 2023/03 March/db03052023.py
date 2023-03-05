"""
Given an integer array, nums, replace each element with the largest value that occurs to the right of it and return the array.
Note: The rightmost element should be replaced with -1.

Ex: Given the following nums…

nums = [5, 2, 3], return [3, 3, -1].
Ex: Given the following nums…

nums = [10, 2, 5, 8, 9], return [9,9,9,9,-1].
"""


class Solution:
    def replaceElements(self, nums: list[int]) -> list[int]:
        """Returns array with each element replaced with largest value to right"""
        mx = -1
        for i in range(len(nums) - 1, -1, -1):
            nums[i], mx = mx, max(mx, nums[i])
        return nums


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.replaceElements([5, 2, 3]))
    print(solution.replaceElements([10, 2, 5, 8, 9]))
