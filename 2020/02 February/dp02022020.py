#  This problem was recently asked by Microsoft:

# Given a list of numbers, and a target number n, find all unique combinations of a, b, c, d, such that a + b + c + d = n.


def fourSum(nums, target):
    # Fill this in.
    n = len(nums)
    nums.sort()
    res = []
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            l = j + 1
            r = n - 1

            while l < r:
                if nums[i] + nums[j] + nums[l] + nums[r] == target:
                    if [nums[i], nums[j], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1

                elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

    return res


print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])
