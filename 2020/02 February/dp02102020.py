# This problem was recently asked by Google:

# Given an integer, find the number of 1 bits it has.


def getSum(n):
    sum = 0
    while n > 0:
        sum += int(n % 10)
        n = int(n / 10)
    return sum


def one_bits(num):
    # Fill this in.
    bits = bin(num)
    n = int(bits[2:])  # remove 0b
    return getSum(n)


print(one_bits(23))
# 4
# 23 = 0b10111
