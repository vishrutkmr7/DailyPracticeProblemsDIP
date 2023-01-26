"""
Given three integer arrays, nums1, nums2, and nums3, sorted in ascending order, return a list containing all integers that
are common to all three arrays.
Note: There are no duplicate values in any of the arrays. 

Ex: Given the following nums1, nums2, and nums3…

nums1 = [1, 2, 3], nums2 = [1, 2], nums3 = [1], return [1].
Ex: Given the following nums1, nums2, and nums3…

nums1 = [4, 5, 6], nums2 = [7, 8, 9], nums3 = [10], return [].
"""
from collections import Counter


class Solution:
    def arraysIntersection(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:
        return [
            key for key, value in Counter(nums1 + nums2 + nums3).items() if value == 3
        ]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.arraysIntersection([1, 2, 3], [1, 2], [1]))
    print(solution.arraysIntersection([4, 5, 6], [7, 8, 9], [10]))
