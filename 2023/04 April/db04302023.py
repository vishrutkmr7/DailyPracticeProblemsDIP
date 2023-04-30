"""
You are given an integer array, ids, that represents a list of product IDs.
Rearrange the array such that no two adjacent product IDs are equal.
Note: It is guaranteed that an answer exists.

Ex: Given the following ids…

ids = [1, 1, 2, 2], return [1, 2, 1, 2] (the ones are separated by the twos.
Note [2, 1, 2, 1] is also an acceptable answer).
Ex: Given the following ids…

ids = [4, 1, 3, 3, 2], return [3, 1, 3, 2, 4].
"""
from collections import Counter


class Solution:
    def rearrange(self, ids: list[int]) -> list[int]:
        if not ids:
            return []
        counts = Counter(ids)
        max_count = max(counts.values())
        if max_count > (len(ids) + 1) // 2:
            return []
        res = [0] * len(ids)
        i = 0
        for id, count in counts.items():
            while count > 0:
                res[i] = id
                count -= 1
                i += 2
                if i >= len(ids):
                    i = 1
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.rearrange([1, 1, 2, 2]))  # [1, 2, 1, 2]
    print(solution.rearrange([4, 1, 3, 3, 2]))  # [3, 1, 3, 2, 4]
