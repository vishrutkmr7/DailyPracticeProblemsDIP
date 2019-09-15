# This problem was recently asked by Microsoft:

# You are given an array of integers.
# Return the largest product that can be made by multiplying
# any 3 integers in the array.

import sys

def maximum_product_of_three(lst):
    # Fill this in.
    n = len(lst)

    if n < 3:
        return -1
    lst.sort()
  
    return max(lst[0] * lst[1] * lst[n - 1],  
               lst[n - 1] * lst[n - 2] * lst[n - 3])

print (maximum_product_of_three([-4, -4, 2, 8]))
# 128
