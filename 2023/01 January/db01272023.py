"""
Given an integer array, nums, return the total number of integers within nums that have an even number of digits. 

Ex: Given the following nums…

nums = [1, 12, 123], return 1 (12 is the only integer with an even number of digits).
Ex: Given the following nums…

nums = [1, 32, 3492, 23], return 3.
"""


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findNumbers([1, 12, 123]))
    print(solution.findNumbers([1, 32, 3492, 23]))
