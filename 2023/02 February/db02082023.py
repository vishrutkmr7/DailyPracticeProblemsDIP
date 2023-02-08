"""
Given a sorted integer array, nums, return the index within nums that the index
is equal to the value at that index. If no such index exists, return -1.

Ex: Given the following nums…

nums = [0, 4, 8], return 0 (zero occurs at the 0th index).
Ex: Given the following nums…

nums = [1, 3, 7, 12], return -1.
"""


class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        ans = [i for i, v in enumerate(nums) if i % 10 == v]
        return min(ans, default=-1)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestEqual([0, 4, 8]))
    print(solution.smallestEqual([1, 3, 7, 12]))
