# This problem was recently asked by Google:

# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
# Challenge: Try sorting the list using constant space.

def sortNums(nums):
    # Fill this in.
    p1 = 0
    p2 = 0
    p3 = len(nums) - 1

    while p2 <= p3:
        if nums[p2] == 1:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1
        elif nums[p2] == 2:
            p2 += 1
        else:
            nums[p2], nums[p3] = nums[p3], nums[p2]
            p3 -= 1

    return nums

print (sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]