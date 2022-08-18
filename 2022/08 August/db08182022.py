"""
This question is asked by Google.
Given a positive integer N, return the number of prime numbers less than N.

Ex: Given the following N…

N = 3, return 1.
2 is the only prime number less than 3.
Ex: Given the following N…

N = 7, return 3.
2, 3, and 5 are the only prime numbers less than 7.
"""


class Solution:
    def find_primes(self, n: int) -> int:
        if n in {0, 1, 2}:
            return 0

        pf = [True] * (n + 1)
        pf[0], pf[1] = False, False
        i = 2
        while i**2 < n:
            if pf[i]:
                j = i**2
                while j < n:
                    pf[j] = False
                    j = j + i

            i += 1
        count = sum(1 for k in range(1, len(pf)) if pf[k])
        return count - 1


# Test Cases
s = Solution()
N = 3
print(s.find_primes(N))  # returns 1.
N = 7
print(s.find_primes(N))  # returns 3.
