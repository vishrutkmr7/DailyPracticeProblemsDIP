"""
Given an integer array, nums, return the length of the longest harmonious subsequence it contains.
Note: A harmonious subsequence is a subsequence in which the difference between the largest value
and the smallest value in the subsequence is exactly one.

Ex: Given the following nums...

nums = [1, 1], return 0.
Ex: Given the following nums...

nums = [3, 4, 5], return 2.
Ex: Given the following nums...

nums = [3, 2, 2, 2, 4, 3, 3], return 6.
"""


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        # O(n) time | O(n) space
        count = 0
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        for num in num_count.items():
            if num[0] + 1 in num_count:
                count = max(count, num_count[num[0]] + num_count[num[0] + 1])

        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findLHS([1, 1]))
    print(solution.findLHS([3, 4, 5]))
    print(solution.findLHS([3, 2, 2, 2, 4, 3, 3]))
