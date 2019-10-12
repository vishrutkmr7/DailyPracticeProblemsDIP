# This problem was recently asked by Microsoft:

# Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list
# using less than 2 * (n - 1) comparisons.


def find_min_max(nums):
    # Fill this in.
    n = len(nums)
    if n % 2 == 0:
        mx = max(nums[0], nums[1])
        mn = min(nums[0], nums[1])
        i = 2
    else:
        mx = mn = nums[0]
        i = 1
    while i < n - 1:
        if nums[i] < nums[i + 1]:
            mx = max(mx, nums[i + 1])
            mn = min(mn, nums[i])
        else:
            mx = max(mx, nums[i])
            mn = min(mn, nums[i + 1])
        i += 2

    return mn, mx


# If n is odd then initialize min and max as first element.
# If n is even then initialize min and max as minimum and maximum of the first two elements respectively.
# For rest of the elements, pick them in pairs and compare their
# maximum and minimum with max and min respectively.

print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
