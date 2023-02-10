"""
Given an integer, n, return the difference between the product and sum of its digits.

Ex: Given the following n…

n = 321, return 0 ((3 * 2 * 1) - (3 + 2 + 1).
Ex: Given the following n…

n = 56, return 19.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n > 0:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10
        return product - total


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.subtractProductAndSum(321))
    print(solution.subtractProductAndSum(56))
