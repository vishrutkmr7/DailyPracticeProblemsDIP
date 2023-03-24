"""
Given positive an integer num, return whether or not it is a perfect square. 

Ex: Given the following num...

num = 9, return true.
Ex: Given the following num...

num = 18, return false.
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r**2 > num:
            r = (r + num / r) // 2
        return r**2 == num


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isPerfectSquare(9) is True
    assert solution.isPerfectSquare(18) is False
    print("All tests passed.")
