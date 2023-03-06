"""
Given an integer array, nums, return an array that represents the classifications of each value within nums.
Note: Classifications start at one, the larger the value in nums, the larger the classification,
two elements that have the same value have the same classification, and classifications should be made as small as possible.

Ex: Given the following nums…

nums = [7, 9, 8], return [1, 3, 2] (7 is the smallest value so its classification is 3, 9 is the largest value so its
classification is 1, and 8 is the second-largest value so its classification is 2).
Ex: Given the following nums…

nums = [2, 9, 3, 5, 7, 4, 4], return [1, 6, 2, 4, 5, 3, 3].
"""


class Solution:
    def arrayRankTransform(self, nums: list[int]) -> list[int]:
        rank = {}
        for i, n in enumerate(sorted(set(nums))):
            if n not in rank:
                rank[n] = i + 1
        return [rank[n] for n in nums]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.arrayRankTransform([7, 9, 8]))
    print(solution.arrayRankTransform([2, 9, 3, 5, 7, 4, 4]))
