# This problem was recently asked by Facebook:

# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.


def findRanges(nums):
    # Fill this in.
    nums = list(set(nums))
    temp = {}
    resArr = []
    for i in nums:
        if i - 1 in temp:
            temp[i - 1] = i
        elif i - 1 in temp.values():
            for key, value in temp.items():
                if i - 1 == value:
                    foundkey = key
            temp[foundkey] = i
        else:
            temp[i] = i

    keylist = sorted(temp.keys())
    resArr.extend(f"{str(key)}->{str(temp[key])}" for key in keylist)
    return resArr


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']

