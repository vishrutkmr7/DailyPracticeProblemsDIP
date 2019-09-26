# This problem was recently asked by Facebook:

# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.


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
        resStr = str(key) + "->" + str(temp[key])
        resArr.append(resStr)

    return resArr


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']

