"""Given a two-dimensional integer array, points, return true if the three points you’re given do not
form a straight line and false otherwise.

Ex: Given the following points…

points = [[1, 1,], [2, 2], [3, 3]], return false.
Ex: Given the following points…

points = [[1, 2], [4, 4], [2, 3]], return true.
"""


class Solution:
    def checkStraightLine(self, points: list[list[int]]) -> bool:
        if len(points) == 2:
            return True

        x1, y1 = points[0]
        x2, y2 = points[1]

        for i in range(2, len(points)):
            x, y = points[i]
            if (y2 - y1) * (x - x1) != (y - y1) * (x2 - x1):
                return False

        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkStraightLine([[1, 1], [2, 2], [3, 3]]))
    print(solution.checkStraightLine([[1, 2], [4, 4], [2, 3]]))
