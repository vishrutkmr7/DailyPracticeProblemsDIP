# This problem was recently asked by Google:

# Given a sorted list of numbers, and two integers low and high representing the lower and upper bound of a range,
# return a list of (inclusive) ranges where the numbers are missing.
# A range should be represented by a tuple in the format of (lower, upper).


def missing_ranges(nums, low, high):
    # Fill this in.
    missing = []
    for i in range(low, high + 1):
        if i not in nums:
            missing.append(i)

    return findRanges(missing)


# From dp09252019.py
def findRanges(nums):
    # Fill this in.
    nums = list(set(nums))
    temp = {}
    resArr = []
    for i in nums:
        if i - 1 in temp.keys():
            temp[i - 1] = i
        elif i - 1 in temp.values():
            for key in temp.keys():
                if i - 1 == temp[key]:
                    foundkey = key
            temp[foundkey] = i
        else:
            temp[i] = i

    keylist = list(temp.keys())
    keylist.sort()
    for key in keylist:
        resStr = (key, temp[key])
        resArr.append(resStr)

    return resArr


print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
