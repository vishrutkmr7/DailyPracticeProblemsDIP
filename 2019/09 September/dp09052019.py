#  This problem was recently asked by Uber:

# You have a landscape, in which puddles can form. You are given an array of non-negative integers representing the elevation
# at each location. Return the amount of water that would accumulate if it rains.


def capacity(arr):
    n = len(arr)
    left = [0] * n
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right = [0] * n
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    return sum(min(left[i], right[i]) - arr[i] for i in range(n))


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
