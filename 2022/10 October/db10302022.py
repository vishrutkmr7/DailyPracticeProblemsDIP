"""
Given an integer array nums and a value, val, remove all instances of val
in-place and return the length of the new array.
Note: It does not matter what values you leave in the array beyond the array’s new length. 
Ex: Given the following nums and val...

nums = [1, 2, 3], val = 2, return 2 (after your modifications your array could look like [1, 3, 3]).
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([1, 2, 3], 2))
