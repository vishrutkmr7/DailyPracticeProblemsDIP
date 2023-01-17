"""
Given an integer array, nums, return all pairs of numbers whose difference equals the minimum difference in the array.

Ex: Given the following nums…

nums = [4, 2, 3], return [[2, 3], [3, 4]] (the minimum difference between any two elements is one and 3 - 2 = 1 and 4 - 3 = 1).
Ex: Given the following nums…

nums = [6, 2, 5, 3, 1], return [[1, 2], [2, 3], [5, 6]].
"""


class Solution:
    def minimumAbsDifference(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        min_diff = min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))
        return [
            [nums[i], nums[i + 1]]
            for i in range(len(nums) - 1)
            if nums[i + 1] - nums[i] == min_diff
        ]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumAbsDifference([4, 2, 3]))
    print(solution.minimumAbsDifference([6, 2, 5, 3, 1]))
