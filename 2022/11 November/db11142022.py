"""
Given a list of nums and a target, return all the unique combinations of nums that sum to target.

Ex: Given the following nums and target...

nums = [8, 2, 2, 4, 5, 6, 3]
target = 9
return [[2,2,5],[2,3,4],[3,6],[4,5]].
"""


class Solution:
    def combinationSum2(self, numbers: list[int], target: int) -> list[list[int]]:
        """Combination Sum 2"""
        numbers.sort()
        result = []
        self.backtrack(numbers, target, 0, [], result)
        return result

    def backtrack(
        self,
        numbers: list[int],
        target: int,
        index: int,
        path: list[int],
        result: list[list[int]],
    ):
        if target == 0:
            result.append(path)
            return

        for i in range(index, len(numbers)):
            if i > index and numbers[i] == numbers[i - 1]:
                continue

            if numbers[i] > target:
                break

            self.backtrack(
                numbers, target - numbers[i], i + 1, path + [numbers[i]], result
            )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2([8, 2, 2, 4, 5, 6, 3], 9))
