# This problem was recently asked by Microsoft:

# Given a list of sorted numbers (can be both negative or positive), return the list of numbers squared in sorted order.


def square_numbers(nums):
    # Fill this in.
    res = [i * i for i in nums]
    res.sort()
    return res

print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
