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
    max_prod =  -(sys.maxsize - 1)

    for i in range(0, n - 2): 
        for j in range(i + 1, n - 1): 
            for k in range(j + 1, n): 
                max_prod = max( 
                    max_prod, lst[i] 
                    * lst[j] * lst[k]) 
  
    return max_prod 

print (maximum_product_of_three([-4, -4, 2, 8]))
# 128
