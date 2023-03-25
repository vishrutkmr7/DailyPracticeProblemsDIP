"""
Given an integer array, nums, return whether or not you can make the array strictly
non-decreasing by modifying at most one element.
Note: A non-decreasing array is an array in which nums[i] <= nums[i + 1] for every i.

Ex: Given the following nums…

nums = [3, 1, 2], return true (you could modify three to one).
Ex: Given the following nums…

nums = [4, 2, 1, 3], return false.
"""


class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkPossibility([3, 1, 2]))
    print(solution.checkPossibility([4, 2, 1, 3]))
