"""
You are given two integer arrays, nums1 and nums2, and asked to sort them in a
particular order. The elements in nums2 are distinct and all occur within nums1.
Sort the elements of nums1 such that the relative ordering of values are the same
as nums2. All elements that don’t appear in nums2 should appear at the end of nums1
in ascending order.
Note: It is guaranteed that no value within nums1 and nums2 exceeds one thousand.

Ex: Given the following nums1 and nums2…

nums1 = [3, 2, 5, 8, 2, 7], nums2 = [7, 8, 3], return [7, 8, 3, 2, 2, 5]
(7, 8, and 3 appear first because of their ordering in nums2 followed by
2 and 5 sorted in ascending order since they don't exist in nums2).
"""


class Solution:
    def relativeSortArray(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return sorted(nums1, key=(nums2 + sorted(nums1)).index)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.relativeSortArray([3, 2, 5, 8, 2, 7], [7, 8, 3]))
