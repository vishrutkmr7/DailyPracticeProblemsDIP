"""
Given an integer N, return the total number self divisible numbers that are strictly less than N (starting from one).
Note: A self divisible number if a number that is divisible by all of its digits.

Ex: Given the following value of N…

N = 17, return 12 because 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15 are all self divisible numbers.
"""


class Solution:
    def selfDividingNumbers(self, n: int) -> list[int]:
        return len(
            [
                i
                for i in range(1, n)
                if all(int(digit) != 0 and i % int(digit) == 0 for digit in str(i))
            ]
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.selfDividingNumbers(17))
