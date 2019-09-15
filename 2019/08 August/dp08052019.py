# This problem was recently asked by Facebook:

# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.
# Try to do it in a single pass of the list.

def two_sum(list1, k):
    # Fill this in.
    for i in list1:
        complementary = k - i
        if complementary in list1:
            return True
    else:
        return "No solution found"

print (two_sum([4,7,1,-3,2], 5))
# True