#  This problem was recently asked by Uber:

# You have a landscape, in which puddles can form. You are given an array of non-negative integers representing the elevation
# at each location. Return the amount of water that would accumulate if it rains.


def capacity(arr):
    # Fill this in.
    n = len(arr)
    left = [0] * n  # height of the tallest bar to the left
    right = [0] * n  # height of the tallest bar to the right

    water = 0

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
