# This problem was recently asked by Apple:

# Given a sorted list of size n, with m unique elements (thus m < n), modify the list such that the first m unique elements in the list will be sorted, ignoring the rest of the list. Your solution should have a space complexity of O(1). Instead of returning the list (since you are just modifying the original list), you should return what m is.


def remove_dups(nums):
    # Fill this in.
    n = len(nums)

    if n == 0 or n == 1:
        return n

    j = 0
    for i in range(0, n - 1):
        if nums[i] != nums[i + 1]:
            nums[j] = nums[i]
            j += 1

    nums[j] = nums[n - 1]
    j += 1

    for k in range(j, n):
        nums.pop()
    return j


nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
# 8
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 9]

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(nums)
# 1
# [1]
