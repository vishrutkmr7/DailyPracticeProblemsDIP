# This problem was recently asked by Amazon:

# Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.


class Solution:
    def intersection(self, nums1, nums2):
        # Fill this in.
        res = [i for i in nums1 if i in nums2]
        res = list(set(res))
        return res


print (Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]