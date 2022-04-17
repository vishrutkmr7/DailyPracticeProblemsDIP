# This problem was recently asked by AirBNB:

# Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.


def findSmallest(nums):
    # Fill this in.
    n = len(nums)
    res = 1
    for i in range(n):
        if nums[i] <= res:
            res = res + nums[i]
        else:
            break
    return res


print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7
