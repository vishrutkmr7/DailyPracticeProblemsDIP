"""
You are given a MxN matrix and a value k. Every value in the matrix is a one
which represents an adult and a zero which represents a child. For every row
in the matrix, adults appear before children. A row that has more adults than
another row is more strongly supervised. Return the k rows of matrix that have
the least amount of supervision in ascending order.
Note: It is guaranteed no ties will occur for the number of adults in a row.

Ex: Given the following matrix and k...

matrix = [
  [1, 1, 0],
  [1, 0, 0],
  [0, 0, 0]
], k = 3, return [2, 1, 0] (row 2 has least adults followed by row 1 and row 0).
Ex: Given the following matrix and k...

matrix = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 0]
], k = 2, return [2, 1].
"""


class Solution:
    def kWeakestRows(self, matrix: list[list[int]], k: int) -> list[int]:
        return [
            i[0]
            for i in sorted(
                [[i, sum(matrix[i])] for i in range(len(matrix))], key=lambda x: x[1]
            )
        ][:k]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.kWeakestRows(
            [
                [1, 1, 0],
                [1, 0, 0],
                [0, 0, 0],
            ],
            3,
        )
    )
    print(
        solution.kWeakestRows(
            [
                [1, 1, 1],
                [1, 1, 0],
                [1, 0, 0],
            ],
            2,
        )
    )
