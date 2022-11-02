"""
Given an array of integers, nums, and a value k, return the kth largest element.

Ex: Given the following array nums…

[1, 2, 3], k = 1, return 3.
Ex: Given the following array nums…

[9, 2, 1, 7, 3, 2], k = 5, return 2.
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return sorted(nums)[-k]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest([1, 2, 3], 1))
    print(solution.findKthLargest([9, 2, 1, 7, 3, 2], 5))
