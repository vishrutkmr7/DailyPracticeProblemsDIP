"""
This question is asked by Google.
Given an array, nums, and an integer k, return whether or not two unique indices exist
such that nums[i] = nums[j] and the two indices i and j are at most  k elements apart.

Ex: Given the following array nums and value k…

nums = [1, 2, 1], k = 1, return false.
Ex: Given the following array nums and value k…

nums = [2, 3, 2], k = 2, return true.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1, 2, 1], 1))
    print(solution.containsNearbyDuplicate([2, 3, 2], 2))
    assert solution.containsNearbyDuplicate([1, 2, 1], 1) is False
    assert solution.containsNearbyDuplicate([2, 3, 2], 2) is True
