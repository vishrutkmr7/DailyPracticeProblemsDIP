#  This problem was recently asked by Apple:

# The Fibonacci sequence is the integer sequence defined by the recurrence relation: F(n) = F(n-1) + F(n-2),
# where F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci numbers.
# Below are the first few values of the sequence:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

# Given a number n, print the n-th Fibonacci Number.


class Solution:
    def fibonacci(self, n):
        # fill this in.
        a = 0
        b = 1
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return a
        elif n == 1:
            return b
        else:
            for _ in range(2, n):
                c = a + b
                a = b
                b = c
            return b


n = 9
print(Solution().fibonacci(n))
# 21
