"""
Given an integer array, nums, return true if there are three consecutive odd values within nums, otherwise, return false.

Ex: Given the following nums…

nums = [1, 2, 3, 4, 5], return false.
Ex: Given the following nums…

nums = [1, 3, 4, 2, 3, 9, 15], return true.
"""


class Solution:
    def threeConsecutiveOdds(self, nums: list[int]) -> bool:
        count = 0
        for i in nums:
            if i % 2 != 0:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False


# Test Cases
if __name__ == "__main__":
    nums = [1, 3, 4, 2, 3, 9, 15]
    print(Solution().threeConsecutiveOdds(nums))
    nums = [1, 2, 3, 4, 5]
    print(Solution().threeConsecutiveOdds(nums))
