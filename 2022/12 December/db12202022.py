"""
Given an array of integers, nums, every value appears three times except one value which only appears
once. Return the value that only appears once.

Ex: Given the following array nums…

nums = [1, 2, 2, 2, 3, 3, 3], return 1.
Ex: Given the following array nums…

nums = [3, 3, 2, 5, 2, 2, 5, 3, 9, 5], return 9.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([1, 2, 2, 2, 3, 3, 3]))
    print(solution.singleNumber([3, 3, 2, 5, 2, 2, 5, 3, 9, 5]))
