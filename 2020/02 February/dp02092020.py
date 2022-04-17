# This problem was recently asked by AirBNB:

# A majority element is an element that appears more than half the time. Given a list with a majority element, find the majority element.


def majority_element(nums):
    # Fill this in.
    n = len(nums)
    maxCount = 0
    index = -1
    for i in range(n):
        count = sum(nums[i] == nums[j] for j in range(n))
        if count > maxCount:
            maxCount = count
            index = i

    return nums[index] if maxCount > n // 2 else "No Majority Element"


print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3
