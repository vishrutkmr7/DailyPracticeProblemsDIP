# This problem was recently asked by LinkedIn:

# You are only allowed to perform 2 operations, multiply a number by 2, or subtract a number by 1. Given a number x and a number y,
# find the minimum number of operations needed to go from x to y.


def min_operations(x, y):
    # Fill this in.
    if x == y:
        return 0

    if x > y:
        return x - y  # subtract -1

    if x > 0 and y < 0:
        return -1  # Not possible

    if y % 2 == 1:  # y is greater and odd
        return int(1 + min_operations(x, y + 1))  # -1 on x or +1 on y
    else:
        return int(1 + min_operations(x, y / 2))  # x * 2  or y / 2


print(min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# print 3
