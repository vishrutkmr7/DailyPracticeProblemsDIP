# This problem was recently asked by Twitter:

# Given an array of characters with repeats, compress it in place.
# The length after compression should be less than or equal to the original array.


class Solution(object):
    def compress(self, chars):
        # Fill this in.
        n = len(chars)
        resDict = {}
        resArr = []
        for i in chars:
            if i not in resDict.keys():
                resDict[i] = 1
            else:
                resDict[i] += 1

        for key in resDict:
            resArr.append(key)
            if resDict[key] > 1:
                resArr.append(resDict[key])

        return resArr


print(Solution().compress(["a", "a", "b", "c", "c", "c"]))
# ['a', '2', 'b', 'c', '3']
