"""
Given an integer array, A, return a new array representing the same number with K added to it.

Ex: Given the following A and K...

A = [1, 2, 3], K = 10, return [1, 3, 3].
Ex: Given the following A and K...

A = [9], K = 3, return [1, 2].
"""


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        n = len(num)
        for i in range(n - 1, -1, -1):
            num[i], k = (num[i] + k) % 10, (num[i] + k) // 10
        return [int(val) for val in str(k)] + num if k != 0 else num


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.addToArrayForm([1, 2, 3], 10))
    print(solution.addToArrayForm([9], 3))
