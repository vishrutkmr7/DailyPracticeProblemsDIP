"""
You are Given an image represented as a matrix. Each value in the matrix represents the color of
an individual pixel. Given a new color represented as an integer and a starting row and column,
transform every adjacent pixel to the starting pixel that has the same color to the new color.
Note: This is effectively implementing a “bucket fill” in a software like Microsoft paint.

Ex: Given the following image, row, column, and color…

image = [
  [0,1,1],
  [0,1,0],
  [1,1,1]
], row = 1, column = 1, color = 3 modify image to be as follows...
image = [
  [0, 3, 3],
  [0, 3, 0],
  [3, 3, 3],
].
"""


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, newColor: int
    ) -> list[list[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] != color:
                return
            image[r][c] = newColor
            if r >= 1:
                dfs(r - 1, c)
            if r + 1 < len(image):
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < len(image[0]):
                dfs(r, c + 1)

        dfs(sr, sc)
        return image


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.floodFill([[0, 1, 1], [0, 1, 0], [1, 1, 1]], 1, 1, 3))
