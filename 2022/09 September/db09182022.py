"""
Given an integer array nums, return an array where each element i represents the product of all
values in nums excluding nums[i].
Note: You may assume the product of all numbers within nums can safely fit within an integer range.

Ex: Given the following array nums…

nums = [1, 2, 3], return [6,3,2].
6 = 3 * 2 (we exclude 1)
3 = 3 * 1 (we exclude 2)
2 = 2 * 1 (we exclude 3)
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3]))
