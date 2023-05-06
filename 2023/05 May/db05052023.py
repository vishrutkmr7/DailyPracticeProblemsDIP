"""
Given an array of integers, nums, and a value k, return whether or not the nums
can be split into k groups such that all values within the group are consecutive.

Ex: Given the following nums and k…

nums = [2, 4, 1, 3], k = 2, return true (the nums can be split into two groups
[1, 2] and [3, 4]).
Ex: Given the following nums and k…

nums = [5, 3, 10], k = 3, return false.
"""


class Solution:
    def splitIntoConsecutiveGroups(self, nums: list[int], k: int) -> bool:
        nums.sort()
        if len(nums) % k != 0:
            return False
        for i in range(0, len(nums), k):
            for j in range(i, i + k - 1):
                if nums[j] + 1 != nums[j + 1]:
                    return False
        return True


# Test Cases
if __name__ == "__main__":
    print(Solution().splitIntoConsecutiveGroups([2, 4, 1, 3], 2))  # True
    print(Solution().splitIntoConsecutiveGroups([5, 3, 10], 3))  # False
