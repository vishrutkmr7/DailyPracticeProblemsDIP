"""
Given an integer array, nums, return the maximum sum that exists between two elements that is less than k. 

Ex: Given the following nums…

nums = [8, 2, 4, 9], k = 13, return 12 (8 + 12 = 12 < 13).
Ex: Given the following nums…

nums = [19, 10, 14, 23, 12], k = 39, return 37.
"""


class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()
        max_sum = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < k:
                max_sum = max(max_sum, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        return max_sum


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSumLessThanK([8, 2, 4, 9], 13))
    print(solution.twoSumLessThanK([19, 10, 14, 23, 12], 39))
