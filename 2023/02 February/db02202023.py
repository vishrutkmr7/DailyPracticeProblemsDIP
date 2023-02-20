"""
Given an integer array, nums, and an integer, k, return whether or not it’s possible to divide nums into groups of size k
where every group contains consecutive numbers.

Ex: Given the following nums and k…

nums = [1, 2, 2, 1], k = 2, return true ([1, 2] and [1, 2]).
Ex: Given the following nums and k…

nums = [1, 2, 3, 3], k = 2, return false.
"""


from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        c = Counter(nums)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(k)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPossibleDivide([1, 2, 2, 1], 2))
    print(solution.isPossibleDivide([1, 2, 3, 3], 2))
