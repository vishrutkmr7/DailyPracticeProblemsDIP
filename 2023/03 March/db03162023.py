"""
Given an integer array, nums, for each nums[i] you need to find the number of elements 
that are strictly smaller than it. Do this for all values in the array and return the
result in an array.

Ex: Given the following nums...

nums = [1, 3], return [0, 1] (1 has 0 elements smaller than it and 3 has 1 element smaller than it).
Ex: Given the following nums...

nums = [4, 2, 9, 10, 3], return [2, 0, 3, 4, 1]
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        temp = sorted(nums)
        mapping = {}
        for i, val in enumerate(temp):
            if val not in mapping:
                mapping[val] = i

        return [mapping[i] for i in nums]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallerNumbersThanCurrent([1, 3]))
    print(solution.smallerNumbersThanCurrent([4, 2, 9, 10, 3]))
