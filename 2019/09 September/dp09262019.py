# This problem was recently asked by Amazon:

# You are given an array of integers. Return an array of the same size where the element at each index
# is the product of all the elements in the original array except for the element at that index.


def products(nums):
    # Fill this in.
    prod = 1
    for i in nums:
        prod *= i

    for i in range(len(nums)):
        nums[i] = int(prod / nums[i])

    return nums


print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
