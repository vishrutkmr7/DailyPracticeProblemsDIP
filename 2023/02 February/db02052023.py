"""
Given an array, nums, every value appears twice except for one which only appears once. The
value that only appears once is the lucky number. Return the lucky number.

Ex: Given the following nums…

nums = [1, 2, 1], return 2.
Ex: Given the following nums…

nums = [1, 3, 1, 2, 2], return 3.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([1, 2, 1]))
    print(solution.singleNumber([1, 3, 1, 2, 2]))
