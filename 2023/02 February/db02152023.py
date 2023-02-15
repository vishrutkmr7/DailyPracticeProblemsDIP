"""Given a two-dimensional integer array, accounts, each row in the matrix represents the total wealth of the ith customer.
The total wealth of a customer is given by the sum of their j account in the ith row. Return the wealth of the richest
customer.

Ex: Given the following accounts…

accounts = [
  [1, 2, 3],
  [4, 5, 6]
], return 15 (4 + 5 + 6 = 15).
Ex: Given the following accounts…

accounts = [
  [1, 2],
  [2, 1]
], return 3.
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(i) for i in accounts)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumWealth([[1, 2, 3], [4, 5, 6]]))
    print(solution.maximumWealth([[1, 2], [2, 1]]))
