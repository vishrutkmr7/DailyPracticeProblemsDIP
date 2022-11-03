"""
Given a list of integers, nums, return a list containing all triplets that sum to zero.

Ex: Given the following nums...

nums = [0], return [].
Ex: Given the following nums...

nums = [0, -1, 1, 1, 2, -2], return [[-2,0,2],[-2,1,1],[-1,0,1]].
"""


class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = v + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([v, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([0]))
    print(solution.threeSum([0, -1, 1, 1, 2, -2]))
