"""
Given a positive integer N, return whether or not it has alternating bit values.

Ex: Given the following value for N…

N = 5, return true.
5 in binary is 101 which alternates bit values between 0 and 1.
Ex: Given the following value for N…

N = 8, return false
8 in binary is 1000 which does not alternate bit values between 0 and 1.
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return all(n >> i & 1 != n >> i + 1 & 1 for i in range(len(bin(n)) - 3))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.hasAlternatingBits(5))
    print(solution.hasAlternatingBits(8))
