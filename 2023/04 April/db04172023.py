"""
Given an array of sorted positive integers, nums, and a value k,
return the kth missing number in nums.

Ex: Given the following nums and k…

nums = [1, 9, 13, 22], k = 4, return 5 (5 is the 4th missing number).
Ex: Given the following nums and k…

nums = [3, 4, 5], k = 2, return 2.
"""


class Solution:
    def findKthPositive(self, nums: list[int], k: int) -> int:
        missing = 0
        for i in range(1, nums[-1]):
            if i not in nums:
                missing += 1
                if missing == k:
                    return i

        return nums[-1] + k - missing


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthPositive([1, 9, 13, 22], 4))
    print(solution.findKthPositive([3, 4, 5], 2))
