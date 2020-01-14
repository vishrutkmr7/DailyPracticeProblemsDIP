# This problem was recently asked by Google:

# Given a list of numbers, for each element find the next element that is larger than the current element.
# Return the answer as a list of indices. If there are no elements larger than the current element, then use -1 instead.


def higherIndex(arr, index):
    for j in range(index, len(arr)):
        if arr[j] > arr[index]:
            return j

    return -1


def larger_number(nums):
    # Fill this in.
    for i in range(0, len(nums)):
        nums[i] = higherIndex(nums, i)

    return nums


print(larger_number([3, 2, 5, 6, 9, 8]))
# [2, 2, 3, 4, -1, -1]
