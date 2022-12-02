"""
You are given an array of integers, nums, that only contains values between one and nums.length
(inclusive). Within nums, some values appear once and some values appear twice. Return a list
containing all numbers between one and nums.length that are missing.

Ex: Given the following nums...

nums = [1, 2, 3, 3], return [4].
Ex: Given the following nums...

nums = [3, 2, 4, 1, 5], return [].
"""


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        For each number i in nums,
        we mark the number that i points as negative.
        Then we filter the list, get all the indexes
        who points to a positive number
        """
        for v in nums:
            index = abs(v) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findDisappearedNumbers([1, 2, 3, 3]))
    print(solution.findDisappearedNumbers([3, 2, 4, 1, 5]))
