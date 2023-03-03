"""
Given an integer, num, return whether or not it is a perfect number.
Note: A perfect number is a positive number that is equal to the sum of its positive divisors
excluding itself.

Ex: Given the following num…

num = 6, return true (1 + 2 + 3 = 6).
Ex: Given the following num…

num = 7, return false.
"""
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        total = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return total == num


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkPerfectNumber(6))
    print(solution.checkPerfectNumber(7))
