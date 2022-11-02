"""
Given an integer array that is sorted in ascending order and a value target,
return two unique indices (one based) such that the values at those indices sums to the given target.
Note: If no two such indices exist, return null. 

Ex: Given the following nums and target…

nums = [1, 2, 5, 7, 9], target = 10, return [1,5].
Ex: Given the following nums and target…

nums = [1, 3, 8], target = 13, return null.
"""


from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = defaultdict(int)
        for i in enumerate(nums):
            diff = target - nums[i[0]]
            if diff in hashMap:
                return [i[0], hashMap[diff]]
            hashMap[nums[i[0]]] = i


if __name__ == "__main__":
    nums = [1, 2, 5, 7, 9]
    target = 10
    print(Solution().twoSum(nums, target))
    nums = [1, 3, 8]
    target = 13
    print(Solution().twoSum(nums, target))
