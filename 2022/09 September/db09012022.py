"""
This question is asked by Apple.
Given an array of numbers, move all zeroes in the array to the end while maintaining
the relative order of the other numbers.
Note: You must modify the array you’re given (i.e. you cannot create a new array).

Ex: Given the following array nums…

nums = [3, 7, 0, 5, 0, 2], rearrange nums to look like the following [3,7,5,2,0,0]
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 7, 0, 5, 0, 2]
    solution.moveZeroes(nums)
    print(nums)
