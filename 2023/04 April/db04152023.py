"""
Given an integer array, nums, you are allowed to perform three moves. A single move consists of
choosing one element in nums and changing it to any other value. Return the minimum possible
difference you can create between the largest and the smallest value in nums after three moves.

Ex: Given the following nums…

nums = [5, 5, 0, 1, 1, 4, 6], return 2 (update 0, 1, and 1 to be 4, then the differece is 6 - 4 = 2).
Ex: Given the following nums…

nums = [4, 5, 20, 14, 19], return 1.
"""


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(
            nums[-4] - nums[0],
            nums[-3] - nums[1],
            nums[-2] - nums[2],
            nums[-1] - nums[3],
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minDifference([5, 5, 0, 1, 1, 4, 6]))
    print(solution.minDifference([4, 5, 20, 14, 19]))
