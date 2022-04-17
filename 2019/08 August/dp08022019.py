# This problem was recently asked by AirBNB:

# Given a sorted array, A, with possibly duplicated elements, 
# find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

class Solution: 
    def getRange(self, arr, target):
        # Fill this in.
        pos = [i for i in range(len(arr)) if arr[i] == target]
        return [pos[0], pos[-1]] if pos else -1
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]