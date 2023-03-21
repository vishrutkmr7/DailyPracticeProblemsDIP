"""
Given an integer array, nums, each value in the array represents a dollar amount.
For every positive value you gain nums[i] dollars and for every negative value you
lose nums[i] dollars. Return the minimum number of dollars you must start with such
that your dollar value never becomes less than one.

Ex: Given the following nums...
nums = [1, -4, 2, -3], return 5 (5 + 1 - 4 + 2 - 3 = 1).
Ex: Given the following nums...

nums = [-10], return 11.
"""


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        min_sum = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)
        return 1 - min_sum


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minStartValue([1, -4, 2, -3]))
    print(solution.minStartValue([-10]))
