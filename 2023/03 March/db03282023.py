"""
Given two non-negative integers low and high, return the total count of odd numbers between them (inclusive).

Ex: Given the following low and high…

low = 1, high = 3, return 2 (1 and 3 are both odd).
Ex: Given the following low and high…

low = 1, high = 10, return 5.
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.countOdds(1, 3))
    print(solution.countOdds(1, 10))
