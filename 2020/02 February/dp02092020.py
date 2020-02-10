# This problem was recently asked by AirBNB:

# A majority element is an element that appears more than half the time. Given a list with a majority element, find the majority element.


def majority_element(nums):
    # Fill this in.
    n = len(nums)
    maxCount = 0
    index = -1
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1

        if count > maxCount:
            maxCount = count
            index = i

    if maxCount > n // 2:
        return nums[index]
    else:
        return "No Majority Element"


print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3
