"""
Given an integer value, N, return the Nth Fibonacci number.
Note: Fibonacci numbers are a number sequence where Fibonacci(N) = Fibonacci(N - 1) + Fibonacci(N - 2). The first two
Fibonacci numbers are zero and one.

Ex: Given the following N…

N = 2, return 1 (one is the second number in the Fibonnaci sequence).
Ex: Given the following N…

N = 3, return 2 (Fibonnaci(3) = Fibonacci(2) + Fibonacci(1) = 1 + 1 = 2).
"""


class Solution:
    def nthFibonacci(self, N: int) -> int:
        if N == 0:
            return 0
        return 1 if N == 1 else self.nthFibonacci(N - 1) + self.nthFibonacci(N - 2)


# Test Cases
if __name__ == "__main__":
    print(Solution().nthFibonacci(2))
    print(Solution().nthFibonacci(3))
