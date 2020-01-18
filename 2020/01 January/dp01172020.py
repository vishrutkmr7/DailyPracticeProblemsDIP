# This problem was recently asked by Amazon:

# Given a positive integer n, find all primes less than n.


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def find_primes(n):
    # Fill this in.
    res = []
    for i in range(2, n + 1):
        if isPrime(i):
            res.append(i)

    return res


print(find_primes(14))
# [2, 3, 5, 7, 11, 13]
