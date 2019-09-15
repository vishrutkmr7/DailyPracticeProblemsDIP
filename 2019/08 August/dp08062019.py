# This problem was recently asked by Facebook:

# Given a list of numbers, where every number shows up twice except for one number, find that one number.

def singleNumber(nums):
    # Fill this in.
    notDup = []
    for i in nums:
        if i in notDup:
            notDup.remove(i)
        else:
            notDup.append(i)

    # since there is only one non duplicate number
    return notDup[0]

print (singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1