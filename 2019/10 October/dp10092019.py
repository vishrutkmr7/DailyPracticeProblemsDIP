# This problem was recently asked by Facebook:

# Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead. Given a list of numbers,
# find the minimum number of jumps to reach the end of the list.


def jumpToEnd(nums):
    # Fill this in.
    n = len(nums)
    jumps = [0 for _ in range(n)]

    if n == 0 or nums[0] == 0:
        return float("inf")

    jumps[0] = 0
    for i in range(1, n):
        jumps[i] = float("inf")
        for j in range(i):
            if (i <= j + nums[j]) and (jumps[j] != float("inf")):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]


print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2
