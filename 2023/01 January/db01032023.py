"""
You are given a special Rubik’s cube that only contains black and white panels. The side of the Rubik’s
cube that is facing you is given as a two-dimensional matrix, cube. Each value in cube is either a
zero or a one where zero represents a black panel and one represents a white panel. Given the cube,
invert it and return the modified cube. Inverting the cube consists of reversing the values in each
row and flipping black values to white and white values to black.

Ex: Given the following cube…

cube = [[1, 0], [0, 1], [1, 1]], return [[1,0],[0,1],[0,0]].
"""


class Solution:
    def invertCube(self, cube: list[list[int]]) -> list[list[int]]:
        for row in cube:
            for value in enumerate(row):
                value = 0 if value == 1 else 1
            row.reverse()
        return cube


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.invertCube([[1, 0], [0, 1], [1, 1]]))
