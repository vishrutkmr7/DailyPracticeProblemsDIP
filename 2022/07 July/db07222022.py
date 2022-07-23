"""
This question is asked by Amazon.
A ship is about to set sail and you are responsible for its safety precautions.
More specifically, you are responsible for determining how many life rafts to carry onboard.
You are given a list of all the passengers’ weights and are informed that
a single life raft has a maximum capacity of limit and can hold at most two weights.
Return the minimum number of life rafts you must take onboard to ensure the safety of all your passengers.
Note: You may assume that a the maximum weight of any individual is at most limit.

Ex: Given the following passenger weights and limit…

weights = [1, 3, 5, 2] and limit = 5, return 3
weights = [1, 2] and limit = 3, return 1
weights = [4, 2, 3, 3] and limit = 5 return 3
"""


class Solution:
    def ship(self, weights, limit):
        weights.sort()
        lo = 0
        hi = len(weights) - 1
        boats = 0
        while lo <= hi:
            if weights[lo] + weights[hi] <= limit:
                lo += 1
            hi -= 1
            boats += 1
        return boats


# Test Cases
print(Solution().ship([1, 3, 5, 2], 5))
print(Solution().ship([1, 2], 3))
print(Solution().ship([4, 2, 3, 3], 5))
