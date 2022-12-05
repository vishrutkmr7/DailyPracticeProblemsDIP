"""
Given an integer array, nums that represents the score of a spelling bee’s contestants,
return string array that represents each of their respective placings.

Ex: Given the following nums…

nums = [3, 1, 4, 2, 5], return ["Bronze Medal","5","Silver Medal","4","Gold Medal"].
"""


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_nums = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        return [
            medals[i] if i < 3 else str(i + 1)
            for i in [sorted_nums.index(num) for num in score]
        ]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findRelativeRanks([3, 1, 4, 2, 5]))
