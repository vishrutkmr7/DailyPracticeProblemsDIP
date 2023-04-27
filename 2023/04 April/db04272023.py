"""
Given a value N, return the Nth "Tresbonacci" value. 
Note: Tresbonacci numbers are a sequence of numbers where
T(N) = T(N -1) + T(N - 2) + T(N - 3). The first three values in the sequence,
T(0), T(1), and T(2) are zero, one, and one respectively.

Ex: Given the following N…

N = 3, return 2 (1 + 1 + 2 = 3).
Ex: Given the following N…

N = 6, return 13.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        t0 = 0
        t1 = 1
        t2 = 1
        for _ in range(n - 2):
            tn = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = tn
        return t2


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.tribonacci(3))  # 2
    print(sol.tribonacci(6))  # 13
    print(sol.tribonacci(7))  # 24
    print(sol.tribonacci(10))  # 149
    print(sol.tribonacci(30))  # 29249425
    print(sol.tribonacci(37))  # 2082876103
    print(sol.tribonacci(38))  # 3831006429
