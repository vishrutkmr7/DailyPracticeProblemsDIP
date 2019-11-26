# This problem was recently asked by Twitter:

# Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.


def findRange(nums):
    # Fill this in.
    n = len(nums)
    e = n - 1
    for s in range(0, n - 1):
        if nums[s] > nums[s + 1]:
            break

    if s == n - 1:
        # Array sorted already
        return (0, 0)

    e = n - 1
    while e > 0:
        if nums[e] < nums[e - 1]:
            break
        e -= 1

    maxL = nums[s]
    minL = nums[s]
    for i in range(s + 1, e + 1):
        if nums[i] > maxL:
            maxL = nums[i]
        if nums[i] < minL:
            minL = nums[i]

    for i in range(s):
        if nums[i] > minL:
            s = i
            break

    i = n - 1
    while i >= e + 1:
        if nums[i] < maxL:
            e = i
            break
        i -= 1

    return s, e


print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)

# Test case 11/25/2019:
print(findRange([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
