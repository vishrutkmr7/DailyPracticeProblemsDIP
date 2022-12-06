"""
Given a sorted array of integers, nums, and a target, return the index of the target within nums.
If it does not exist, return the index of where target should be inserted.

Ex: Given the following nums and target...

nums = [1, 5, 8, 12], target = 12, return 3.
Ex: Given the following nums and target...

nums = [3, 4, 7, 12, 29], target = 5, return 2.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)


if __name__ == "__main__":
    nums = [1, 5, 8, 12]
    target = 12
    print(Solution().searchInsert(nums, target))

    nums = [3, 4, 7, 12, 29]
    target = 5
    print(Solution().searchInsert(nums, target))
