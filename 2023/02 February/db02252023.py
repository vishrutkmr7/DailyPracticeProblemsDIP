"""
You are given two integer arrays, A and B. B is an anagram of A meaning that B contains all the same elements of A but in a different order.
Return an array that represents a mapping from every element in A to which index it occurs at in B.
Note: You may assume every element in A is unique.

Ex: Given the following A and B…

A = [8, 23, 2], B = [2, 23, 8], return [2, 1, 0] (8 appears at index 2 in B, 23 appears at index 1 in B, and 2 appears at index 0 in B).
Ex: Given the following A and B…

A = [9, 3, 1, 5, 2, 4], B = [2, 5, 1, 3, 4, 9], return [5,3,2,1,0,4].
"""


class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {nums2[i]: i for i, _ in enumerate(nums2)}
        return [d[a] for a in nums1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.anagramMappings([8, 23, 2], [2, 23, 8]))
    print(solution.anagramMappings([9, 3, 1, 5, 2, 4], [2, 5, 1, 3, 4, 9]))
