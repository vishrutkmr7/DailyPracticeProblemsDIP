"""
Given a non-empty integer array, nums, return the minimum number of moves to make all
values in nums equal. A move consists of incrementing all but one element in the array by one.

Ex: Given the following nums...

nums = [1, 2, 3], return 3. [1, 2, 3] -> [2, 3, 3] -> [3, 4, 3] -> [4, 4, 4].
"""


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.minMoves([1, 2, 3]))
