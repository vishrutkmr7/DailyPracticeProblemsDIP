# This problem was recently asked by Twitter:

# Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit, up til the 31st and 32nd bit.


def swap_bits(x):
    # Fill this in.
    # The number 0xAAAAAAAA is a 32 bit number with all even bits set as 1 and all odd bits as 0.
    even_bits = x & 0xAAAAAAAA

    # The number 0x55555555 is a 32 bit number with all odd bits set as 1 and all even bits as 0.
    odd_bits = x & 0x55555555

    # Right shift even bits
    even_bits >>= 1

    # Left shift odd bits
    odd_bits <<= 1

    # Combine even and odd bits
    return even_bits | odd_bits


print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101

# Solution from: https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/
