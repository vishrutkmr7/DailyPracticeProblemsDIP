#  This problem was recently asked by Apple:

# Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number.
# Your solution should ideally be O(n) time and use constant extra space.


class Solution(object):
    def findSingle(self, nums):
        # Fill this in.
        dup = []
        n = len(nums)
        for i in range(0, n):
            if nums[i] not in dup:
                dup.append(nums[i])
            else:
                dup.remove(nums[i])

        return dup[0]


nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
