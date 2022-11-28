"""
Given two integer arrays, nums1 and nums2, return the intersection of the two arrays
(i.e. the elements they have in common).

Ex: Given the following nums1 and nums2...

nums1 = [1, 2, 2, 3], nums2 = [0, 2, 2, 5], return [2, 2].
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.intersect([1, 2, 2, 3], [0, 2, 2, 5]))
