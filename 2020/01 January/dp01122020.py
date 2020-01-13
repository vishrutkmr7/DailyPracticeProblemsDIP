# This problem was recently asked by AirBNB:

# Given a list of sorted numbers, and two integers k and x, find k closest numbers to the pivot x.


def closest_nums(nums, k, x):
    # Fill this in.
    diffArr = []
    for i in nums:
        diffArr.append(abs(x - i))

    diffArr.sort()
    diffArr = diffArr[:k]

    res = []
    for j in diffArr:
        if x + j in nums and x + j not in res:
            res.append(x + j)
        elif x - j in nums and x - j not in res:
            res.append(x - j)

    return res


print(closest_nums([1, 3, 7, 8, 9], 3, 5))
# [7, 3, 8]
