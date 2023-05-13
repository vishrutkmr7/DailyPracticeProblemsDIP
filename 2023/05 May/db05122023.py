"""
You walk into a coffee shop that serves all of the given customers. At the ith minute,
customers[i] customers are in the shop. The barista is stressed at the ith minute if
stressed[i] = 1 and calm otherwise. Customers that are in the shop while the barista
is stressed are unhappy. Customers that are in the shop while the barista is not stressed
are happy. The barista knows how to remain calm for a duration of minutes, but can only
do so once. Return the maximum number of customers that can be happy.

Ex: Given the following customers, stressed, and duration…

customers = [3, 1, 2], stressed = [1, 0, 0], duration = 1, return 6 (the barista can remain calm for the first minute making all the customers happy 3 + 1 + 2 = 6).
Ex: Given the following customers, stressed, and duration…

customers = [5, 2, 4, 3], stressed = [1, 1, 0, 1], duration = 2, return 11 (5 + 2 + 4).
"""


class Solution:
    def maxHappyCustomers(self, customers: list[int], grumpy: list[int], X: int) -> int:
        i = win_of_make_satisfied = satisfied = max_make_satisfied = 0
        for c, g in zip(customers, grumpy):
            satisfied += (1 - g) * c
            win_of_make_satisfied += g * c
            if i >= X:
                win_of_make_satisfied -= grumpy[i - X] * customers[i - X]
            max_make_satisfied = max(win_of_make_satisfied, max_make_satisfied)
            i += 1
        return satisfied + max_make_satisfied


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.maxHappyCustomers([3, 1, 2], [1, 0, 0], 1) == 6
