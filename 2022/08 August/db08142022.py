"""
This question is asked by Amazon.
Given an array that contains all distinct values from zero through N except one number,
return the number that is missing from the array.

Ex: Given the following array nums…

nums = [1, 4, 2, 0], return 3.
3 is the only number missing in the array between 0 and 4.

Ex: Given the following array nums…

nums = [6, 3, 1, 2, 0, 5], return 4.
4 is the only number missing in the array between 0 and 6.
"""


class Solution:
    def findMissingNumber(self, nums):
        if 0 not in nums:
            return 0
        if len(nums) == 1:
            return 1
        n = max(nums)
        AP_sum = n * (n + 1) / 2
        nums_sum = sum(nums)
        return int(n + 1 if AP_sum == nums_sum else AP_sum - nums_sum)


# Test Cases
print(Solution().findMissingNumber([1, 4, 2, 0]))
print(Solution().findMissingNumber([6, 3, 1, 2, 0, 5]))
