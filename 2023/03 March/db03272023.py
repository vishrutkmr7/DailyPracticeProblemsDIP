"""
You are given an image represented as an MxN matrix where each value represents a pixel.
Modify each pixel in the image such that its the average of its eight neighbors and return
the modified image.
Note: If a pixel does not have eight neighbors, use as many neighbors as possible.

Ex: Given the following image…

image = [
  [1, 0],
  [1, 0]
], return the image to be modified as follows...
image = [
  [0, 0],
  [0, 0]
].
Ex: Given the following image…

image = [
  [1, 3, 2],
  [5, 8, 3],
  [4, 2, 2]
], return the image to be modified as follows...
image = [
  [4, 3, 4],
  [3, 3, 3],
  [4, 4, 3]
].
"""

from itertools import product


class Solution:
    def imageSmoother(self, image: list[list[int]]) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in product(range(m), range(n)):
            count = 0
            for x, y in product(
                range(max(0, i - 1), min(m, i + 2)), range(max(0, j - 1), min(n, j + 2))
            ):
                result[i][j] += image[x][y]
                count += 1
            result[i][j] = result[i][j] // count
        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.imageSmoother(
            [
                [1, 0],
                [1, 0],
            ]
        )
    )
    print(
        solution.imageSmoother(
            [
                [1, 3, 2],
                [5, 8, 3],
                [4, 2, 2],
            ]
        )
    )
