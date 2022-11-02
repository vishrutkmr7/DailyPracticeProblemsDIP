"""
Given an integer array, nums, return the total number of “partners” in the array.
Note: Two numbers in our array are partners if they reside at different indices and both contain the same value.

Ex: Given the following array nums…

nums = [5, 5, 3, 1, 1, 3, 3], return 5.
5 (index 0) and 5 (index 1) are partners.
1 (index 3) and 1 (index 4) are partners.
3 (index 2) and 3 (index 5) are partners.
3 (index 2) and 3 (index 6) are partners.
3 (index 5) and 3 (index 6) are partners.
"""


class Solution:
    def countPartners(self, nums: list[int]) -> int:
        count = 0
        for i in enumerate(nums):
            for j in range(i[0] + 1, len(nums)):
                if nums[i[0]] == nums[j]:
                    count += 1
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.countPartners([5, 5, 3, 1, 1, 3, 3]) == 5
    print("All tests passed.")
