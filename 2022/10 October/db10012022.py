"""
Given an array of integers, nums, each element in the array either appears once or twice.
Return a list containing all the numbers that appear twice.
Note: Each element in nums is between one and nums.length (inclusive).

Ex: Given the following array nums…

nums = [2, 3, 1, 5, 5], return [5].
Ex: Given the following array nums…

nums = [1, 2, 3], return [].
Ex: Given the following array nums…

nums = [7, 2, 2, 3, 3, 4, 4], return [2,3,4].
"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        return [i for i, value in dic.items() if value > 1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findDuplicates([2, 3, 1, 5, 5]))
    print(solution.findDuplicates([1, 2, 3]))
    print(solution.findDuplicates([7, 2, 2, 3, 3, 4, 4]))
