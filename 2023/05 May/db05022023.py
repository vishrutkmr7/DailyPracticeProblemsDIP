"""
Given two values, low and high, return all values between low and high (inclusive) that contain
consecutive digits in sorted order.
Note: low and high will be between one and a million.

Ex: Given the following low and high…

low = 10, high = 25, return [12, 23].
Ex: Given the following low and high…

low = 15, high = 48, return [23, 34, 45].
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res = []
        for i in range(1, 9):
            num = i
            for j in range(num + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    res.append(num)
        return sorted(res)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.sequentialDigits(10, 25) == [12, 23]
    assert solution.sequentialDigits(15, 48) == [23, 34, 45]
    print("Success")
