"""
Given a value, N, you are asked to form a staircase. The number of elements
in each row of the staircase must match the current row. Return the total number
of full staircase rows you can create.

Ex: Given the following N...

N = 3 return 2.
*
* * (this staircase has two rows)
Ex: Given the following N...

N = 7 return 3.
*
* *
* * *
* (this row is not full)
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2 * n + 0.25) ** 0.5 - 0.5)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.arrangeCoins(3))
    print(solution.arrangeCoins(7))
