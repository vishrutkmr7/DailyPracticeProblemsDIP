# This problem was recently asked by Google:

# Given a list of numbers and a target number n, find 3 numbers in the list that sums closest to the target number n.
# There may be multiple ways of creating the sum closest to the target number, you can return any combination in any order.


def closest_3sum(nums, target):
    # Fill this in.
    nums.sort()
    closest_sum = 2 ** 31 - 1
    n1 = 0
    n2 = 0
    n3 = 0
    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1
        while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]
            if curr_sum == target:
                return [nums[i], nums[j], nums[k]]
            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum
                n1 = i
                n2 = j
                n3 = k
            if curr_sum < target:
                j = j + 1
            else:
                k = k - 1

    return [nums[n1], nums[n2], nums[n3]]


print(closest_3sum([2, 1, -5, 4], -1))
# Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# print [-5, 1, 2]
