# This problem was recently asked by Uber:

# Given a list of possible coins in cents, and an amount (in cents) n,
# return the minimum number of coins needed to create the amount n.
# If it is not possible to create the amount using the given coin denomination, return None.


import sys


def make_change(coins, n):
    # Fill this in.
    if n == 0:
        return 0
    m = len(coins)
    res = sys.maxsize
    for i in range(0, m):
        if coins[i] <= n:
            sub_res = make_change(coins, n - coins[i])
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1

    return res


print(make_change([1, 5, 10, 25], 36), "coins")
# 3 coins (25 + 10 + 1)
