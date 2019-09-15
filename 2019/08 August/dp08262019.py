# This problem was recently asked by Facebook:

# Given an array nums, write a function to move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

class Solution:
    def moveZeros(self, nums):
        # Fill this in.
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        # Make the rest of the elements from count to end = 0, as non 0s have been shifted 
        while count < n:
            nums[count] = 0
            count += 1

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
