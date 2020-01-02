# This problem was recently asked by Facebook:

# Given a number n, find the least number of squares needed to sum up to the number.


def square_sum(n):
    # Fill this in.
    if n <= 3:
        return n

    res = n

    for x in range(1, n + 1):
        temp = x * x
        if temp > n:
            break
        else:
            res = min(res, 1 + square_sum(n - temp))

    return res


print(square_sum(13))
# Min sum is 3^2 + 2^2
# 2
