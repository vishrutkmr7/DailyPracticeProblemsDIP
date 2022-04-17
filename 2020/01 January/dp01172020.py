# This problem was recently asked by Amazon:

# Given a positive integer n, find all primes less than n.


def isPrime(n):
    return False if n <= 1 else all(n % i != 0 for i in range(2, n))


def find_primes(n):
    return [i for i in range(2, n + 1) if isPrime(i)]


print(find_primes(14))
# [2, 3, 5, 7, 11, 13]
