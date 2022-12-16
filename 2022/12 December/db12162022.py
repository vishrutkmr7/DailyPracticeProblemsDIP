"""
Given an array of integers, nums, duplicate the occurrence of each zero in the array by shifting
other non-zero elements to the right.
Note: The modification to nums must be done in-place, do not return anything from your function,
and elements beyond the length of the original array not not written.

Ex: Given the following nums...

nums = [1, 0, 4, 0, 5, 8], return null but nums should look as follows after your function runs
[1,0,0,4,0,0].
Ex: Given the following nums...

nums = [1, 4, 9], return null but nums should look as follows after your function runs [1, 4, 9].
"""


class Solution:
    def duplicateZeros(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.insert(i, 0)
                nums.pop()
                i += 1
            i += 1


# Test Cases
if __name__ == "__main__":
    nums = [1, 0, 4, 0, 5, 8]
    Solution().duplicateZeros(nums)
    print(nums)
    nums = [1, 4, 9]
    Solution().duplicateZeros(nums)
    print(nums)
