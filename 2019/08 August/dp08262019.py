# This problem was recently asked by Facebook:

# Given an array nums, write a function to move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

class Solution:
    def moveZeros(self, nums):
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter += 1
            elif i != 0:
                temp = abs(i-counter)
                nums[temp] = nums[i]
                nums[i] = 0

        return nums

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
