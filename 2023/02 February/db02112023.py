"""
Given a non-negative integer array, nums, return the maximum product you can create with two separate indices
i and j.
Note: You may assume the product will not overflow.

Ex: Given the following nums…

nums = [4, 2, 5, 3], return 20 (5 * 4).
Ex: Given the following nums…

nums = [6, 2, 4, 3], return 24.
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1]) * (nums[-2])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([4, 2, 5, 3]))
    print(solution.maxProduct([6, 2, 4, 3]))
