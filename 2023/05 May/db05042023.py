"""
Given an array of integers, nums, return the minimum number of operations needed to make
every value in nums unique.
Note: An operation consists of selecting a value in nums and incrementing it by one.

Ex: Given the following nums…

nums = [2, 2, 1, 3], return 2 (increment one of the twos twice or increment one 2 once and
the 3 once).
Ex: Given the following nums…

nums = [4, 1, 2], return 0 (no operations are needed).
"""


class Solution:
    def minOperations(self, nums):
        nums.sort()
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                count += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([2, 2, 1, 3]))  # 2
    print(solution.minOperations([4, 1, 2]))  # 0
