"""
Given a k-digit integer, num, return whether or not the number if magical.
Note: A magical numbers is a number in which the sum of all its digits
raised to the kth power sum to the number itself.

Ex: Given the following num…

num = 153, return true (1^3 + 5^3 + 3^3 = 153).
Ex: Given the following num…

num = 38, return false.
"""


class Solution:
    def isMagical(self, num: int) -> bool:
        return num == sum(int(digit) ** len(str(num)) for digit in str(num))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isMagical(153) is True
    assert solution.isMagical(38) is False
    print("All tests passed successfully.")
