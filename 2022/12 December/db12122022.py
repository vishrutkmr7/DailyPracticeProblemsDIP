"""
Given an integer array, nums, return the largest unique value in nums.

Ex: Given the following nums…

nums = [4, 9, 2, 9], return 4.
Ex: Given the following nums…

nums = [8, 1, 10, 1, 4, 8, 4, 10], return -1.
"""


class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return next((nums[i] for i in range(len(nums)) if nums.count(nums[i]) == 1), -1)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestUniqueNumber([4, 9, 2, 9]))
    print(solution.largestUniqueNumber([8, 1, 10, 1, 4, 8, 4, 10]))
