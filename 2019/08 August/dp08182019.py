# This problem was recently asked by Amazon:

# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.

class Solution:
    def minSubArrayLen(self, nums, s):
        # Fill this in
        n = len(nums)
        res = n + 1 # Initialize

        for start in range(n):
            curr_sum = nums[start]
            if curr_sum > s:
                return 1

            for end in range(start + 1, n):
                curr_sum += nums[end]
                if curr_sum > s and (end - start) < res:
                    res = end - start

        if res == n + 1:
            return 0

        return res

print (Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
