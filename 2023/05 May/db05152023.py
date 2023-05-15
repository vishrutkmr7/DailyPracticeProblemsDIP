"""
You are given N dice, where each die has max faces (with values one through max, and an integer,
target. Return the total number of ways you can roll the N dice such that the sum of all their
face-up values equals the given target.

Ex: Given the following, N, max, and target…

N = 1, max = 6, target = 5, return 1 (there is only one way to roll the single die to sum to 5 i.e.
roll a 5).
Ex: Given the following, N, max, and target…

N = 2, max = 6, target = 4, return 3.
"""


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        cache = {}

        def dp(left, target):
            if target < 0:
                return 0
            if left == 0:
                return 1 if target == 0 else 0
            if (left, target) in cache:
                return cache[(left, target)]

            ways = 0
            for i in range(1, k + 1):
                ways += dp(left - 1, target - i)
                ways %= MOD
            cache[(left, target)] = ways
            return ways

        return dp(n, target)


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    assert sol.numRollsToTarget(1, 6, 5) == 1
    assert sol.numRollsToTarget(2, 6, 4) == 3
    # assert sol.numRollsToTarget(30, 30, 500) == 222616187
    print("Passed all tests!")
