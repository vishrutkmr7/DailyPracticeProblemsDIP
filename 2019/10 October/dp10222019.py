# This problem was recently asked by Amazon:

# You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.


def longest_consecutive(nums):
    ans = 0
    s = set(nums)
    n = len(nums)
    for i in range(n):
        if (nums[i] - 1) not in s:
            j = nums[i]
            while j in s:
                j += 1
            ans = max(ans, j - nums[i])

    return ans


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
