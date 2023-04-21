"""
Given a positive integer, N, return all flippable numbers between one and N inclusive.
Note: A flippable number is a number whose digits can be rotated 180 degrees to form a
different number. Digits 0, 1, 6, 8, and 9 become 0, 1, 9, 8, and 6 respectively when
rotated. Digits 2, 3, 4, 5, and 7 are invalid when rotated.

Ex: Given the following value N…

N = 10, return 3 (6, 9, and 10 are flippable).
Ex: Given the following value N…

N = 17, return 4.
"""


class Solution:
    def rotatedDigits(self, N: int) -> int:
        return sum(bool(self.isFlippable(i)) for i in range(1, N + 1))

    def isFlippable(self, num: int) -> bool:
        flippable = False
        while num > 0:
            digit = num % 10
            if digit in [3, 4, 7]:
                return False
            if digit in [2, 5, 6, 9]:
                flippable = True
            num //= 10
        return flippable


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.rotatedDigits(10))
    print(solution.rotatedDigits(17))
