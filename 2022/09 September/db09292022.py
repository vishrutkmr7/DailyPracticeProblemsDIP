"""
Given an array nums, return the third largest (distinct) value.
Note: If the third largest number does not exist, return the largest value.

Ex: Given the following array nums…

nums = [1, 4, 2, 3, 5], return 3.
Ex: Given the following array nums…

nums = [2, 3, 3, 5], return 2.
Ex: Given the following array nums…

nums = [9, 5], return 9."""


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        return nums[-3] if len(nums) >= 3 else nums[-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.thirdMax([1, 4, 2, 3, 5]))
    print(solution.thirdMax([2, 3, 3, 5]))
    print(solution.thirdMax([9, 5]))
