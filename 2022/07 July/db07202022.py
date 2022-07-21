"""
This question is asked by Apple.
Given a list of positive numbers without duplicates and a target number,
find all unique combinations of the numbers that sum to the target. Note: You may use the same number more than once.

Ex: Given the following numbers and target…

numbers = [2,4,6,3], target = 6,
return [
    [2,2,2],
    [2,4],
    [3,3],
    [6]
]
"""
import itertools


class Solution:
    def combinationSum(self, numbers, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(numbers) or total > target:
                return

            cur.append(numbers[i])
            dfs(i, cur, total + numbers[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    def combinationSum2(self, numbers, target):
        res = [
            list(seq)
            for i in range(len(numbers), 0, -1)
            for seq in itertools.combinations(numbers, i)
            if sum(seq) == target
        ]
        for num in numbers:
            if target % num == 0 and [num] * (target // num) not in res:
                res.append([num] * (target // num))

        return res


# Test Cases
print(Solution().combinationSum([2, 4, 6, 3], 6))
