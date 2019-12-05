#  This problem was recently asked by Amazon:

# Given a 32 bit integer, reverse the bits and return that number.


def to_bits(n):
    return "{0:08b}".format(n)


def reverse_num_bits(num):
    # Fill this in.
    binary = to_bits(num)
    reverse = binary[::-1]
    reverse = reverse + (32 - len(reverse)) * "0"
    # Bitsize = 32
    return int(reverse, 2)


print(to_bits(1234))
# 10011010010
print(reverse_num_bits(1234))
# 1260388352
print(to_bits(reverse_num_bits(1234)))
# 1001011001000000000000000000000
