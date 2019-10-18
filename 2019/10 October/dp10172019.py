#  This problem was recently asked by LinkedIn:

# Given a string, rearrange the string so that no character next to each other are the same.
# If no such arrangement is possible, then return None.
import math, operator


def rearrangeString(s):
    # Fill this in.
    n = len(s)
    freqDict = {}
    for i in s:
        if i not in freqDict.keys():
            freqDict[i] = 1
        else:
            freqDict[i] += 1

    for j in list(freqDict.values()):
        if j > math.ceil(n / 2):
            return None

    return maxArrange(freqDict)[:-4]


temp = ""


def maxArrange(inp):
    global temp
    n = len(inp)
    if list(inp.values()) != [0] * n:
        resCh = max(inp.items(), key=operator.itemgetter(1))[0]
        if resCh is not None and resCh != temp:
            inp[resCh] -= 1
            # Terminates with None
            temp = resCh
            return resCh + str(maxArrange(inp))


print(rearrangeString("abbccc"))
# cbcabc
