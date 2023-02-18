"""
Given an integer array, nums, return whether or not you can split the array into three subarrays all of which have
an equal sum.

Ex: Given the following nums…

nums = [2, 3, 9, 9, 3, 2, 3, 2, 9], return true.
Ex: Given the following nums…

nums = [1, 2, 3], return false.
"""


class Solution:
    def canThreePartsEqualSum(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 3 != 0:
            return False
        target = total // 3
        count = 0
        temp = 0
        for num in nums:
            temp += num
            if temp == target:
                count += 1
                temp = 0
        return count >= 3


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.canThreePartsEqualSum([2, 3, 9, 9, 3, 2, 3, 2, 9]))
    print(solution.canThreePartsEqualSum([1, 2, 3]))
