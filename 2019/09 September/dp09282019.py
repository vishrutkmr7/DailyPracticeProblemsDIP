# This problem was recently asked by Microsoft:

# You are given an array of integers. Return the length of the longest increasing subsequence
# (not necessarily contiguous) in the array.


def LIS(nums):
    n = len(nums)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


print(LIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
# 6
