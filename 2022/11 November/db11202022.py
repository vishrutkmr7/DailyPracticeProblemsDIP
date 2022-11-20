"""
Given an sorted integer array, nums, that has been rotated at an unknown index,
return the minimum value.
Note: The array only contains unique values. 

Ex: Given the following array nums...

nums = [7, 9, 10, 2, 4, 6], return 2.
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin([7, 9, 10, 2, 4, 6]))
