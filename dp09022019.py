# This problem was recently asked by Twitter:

# You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.


def max_subarray_sum(arr):
    # Fill this in.
    n = len(arr)
    local_max = 0
    global_max = 0
    # Kadane's Algorithm
    for i in range(0, n):
        local_max = max(arr[i], arr[i] + local_max)
        if local_max > global_max:
            global_max = local_max

    return global_max


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
