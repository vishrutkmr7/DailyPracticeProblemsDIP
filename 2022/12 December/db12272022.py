"""
Given an integer array, nums, return a list containing all subsets of nums that contain at least two elements and have an
increasing sequence.

Ex: Given the following nums…

nums = [1, 2, 3], return [[1,2],[1,2,3],[1,3],[2,3]].
Ex: Given the following nums…

nums = [2, 4, 3, 5], return [[2,4],[2,4,5],[2,3],[2,3,5],[2,5],[4,5],[3,5]].
"""


from itertools import combinations


class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        return [
            list(x)
            for i in range(2, len(nums) + 1)
            for x in set(combinations(nums, i))
            if all(a <= b for a, b in zip(x, x[1:]))
        ]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubsequences([1, 2, 3]))
    print(solution.findSubsequences([2, 4, 3, 5]))
