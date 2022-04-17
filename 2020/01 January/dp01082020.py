# This problem was recently asked by Apple:

# Given a non-negative integer n, convert n to base 2 in string form. Do not use any built in base 2 conversion functions like bin.


def base_2(n):
    # Fill this in.
    return "" if n == 0 else base_2(n // 2) + str(n % 2)


print(base_2(123))
# 1111011
