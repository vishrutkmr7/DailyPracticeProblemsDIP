# This problem was recently asked by Twitter:

# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that
# a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.


class Solution(object):
    def threeSum(self, nums):
        # Fill this in.
        n = len(nums)
        found = False
        nums.sort()
        ans = []

        for i in range(n - 1):
            l = i + 1
            r = n - 1
            x = nums[i]
            while l < r:
                if (x + nums[l] + nums[r]) == 0:
                    p = [x, nums[l], nums[r]]
                    if p not in ans:
                        ans.append(p)
                    l += 1
                    r -= 1
                    found = True
                elif (x + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    r -= 1

        return ans if found else "No Triplets found"


# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
