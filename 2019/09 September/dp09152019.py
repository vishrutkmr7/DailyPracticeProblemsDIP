#  This problem was recently asked by Apple:

# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library’s sort function for this problem.
# Can you do this in a single pass?


class Solution:
    def sortColors(self, nums):
        # Fill this in.
        n = len(nums)
        n0 = 0
        n1 = 1
        n2 = 2
        for i in nums:
            if i == 0:
                n0 += 1
            elif i == 1:
                n1 += 1
            elif i == 2:
                n2 += 1

        n1 = n0 + n1
        n2 = n1 + n2

        for i in range(n):
            if i < n0:
                nums[i] = 0
            elif i < n1:
                nums[i] = 1
            elif i < n2:
                nums[i] = 2


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
