"""
Given a set of points, where each element is an integer array containing an x and y value,
return whether or not all the points exist on the same line.

Ex: Given the following points…

points = [[1, 2], [3, 2]], return true.
Ex: Given the following points...

points = [[1, 2], [3, 2], [-1, -1]], return false.
"""


class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y2 - y1) * (x - x1) != (y - y1) * (x2 - x1):
                return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkStraightLine([[1, 2], [3, 2]]))
    print(solution.checkStraightLine([[1, 2], [3, 2], [-1, -1]]))
