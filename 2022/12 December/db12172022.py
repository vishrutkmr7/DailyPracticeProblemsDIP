"""
Given a non-negative integer x, return its square root.
Note: You may not use a built in square root function and decimals should be truncated to return an
integer value.

Ex: Given the following x...

x = 9, return 3.
Ex: Given the following x...

x = 12, return 3.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)

    def mySqrtBinSearch(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrtBinSearch(9))
    print(solution.mySqrtBinSearch(12))
