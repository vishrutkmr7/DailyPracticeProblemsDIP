# This problem was recently asked by Twitter:

# Given an array of integers of size n, where all elements are between 1 and n inclusive,
# find all of the elements of [1, n] that do not appear in the array. Some numbers may appear more than once.


class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Fill this in.
        n = len(nums)
        ans = []
        for i in range(1, n):
            if i not in nums:
                ans.append(i)

        return ans


nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
