"""
Given an integer array, nums, return whether or not the array was originally
sorted in non-decreasing order and then rotated some number of positions.

Ex: Given the following nums…

nums = [4, 5, 1, 2, 3], return true (values 4 and 5 were rotated to the beginning
of the array).
Ex: Given the following nums…

nums = [4, 5, 1, 2, 3, 6], return false.
"""


class Solution:
    def check(self, nums: list[int]) -> bool:
        return sum(a > b for a, b in zip(nums, nums[1:] + nums[:1])) <= 1


# Test Cases
if __name__ == "__main__":
    print(Solution().check([4, 5, 1, 2, 3]))
    print(Solution().check([4, 5, 1, 2, 3, 6]))
    print(Solution().check([4, 5, 6, 1, 2, 3]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 7]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 0]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 4]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 5]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 6]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 7]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 8]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 9]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 10]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 11]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 12]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 13]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 14]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 15]))
    print(Solution().check([4, 5, 6, 1, 2, 3, 16]))
