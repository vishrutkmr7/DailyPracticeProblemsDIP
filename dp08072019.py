# This problem was recently asked by Microsoft:

# You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
# Can you find a solution in O(n) time?

def check(lst):
    # Fill this in.
    p = None
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            if p is not None:
                return False
            p = i
    
    # credit to https://leetcode.com/articles/non-decreasing-array/
    return (p is None or p == 0 or p == len(lst)-2 or lst[p-1] <= lst[p+1] or lst[p] <= lst[p+2])
  
print (check([13, 4, 7]))
# True
print (check([5,1,3,2,5]))
# False