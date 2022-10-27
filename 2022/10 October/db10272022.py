"""
Given an integer n, return whether or not it is a power of three. 

Ex: Given the following value for n...

n = 9, return true
Ex: Given the following value for n...

n = 50, return false
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n >= 1 and 3**20 % n == 0


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isPowerOfThree(9) == True
    assert solution.isPowerOfThree(50) == False
    print("All tests passed.")
