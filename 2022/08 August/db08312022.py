"""
This question is asked by Facebook.
Given N points on a Cartesian plane, return the minimum time required to visit all points in the order that they’re given.
Note: You start at the first point and can move one unit vertically, horizontally, or diagonally in a single second.

Ex: Given the following points…

points = [[0, 0], [1,1], [2,2]], return 2.
In one second we can travel from [0, 0] to [1, 1]
In another second we can travel from [1, 1,] to [2, 2]
Ex: Given the following points…

points = [[0, 1], [2, 3], [4, 0]], return 5.
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        return sum(
            max(
                abs(points[i][0] - points[i + 1][0]),
                abs(points[i][1] - points[i + 1][1]),
            )
            for i in range(len(points) - 1)
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minTimeToVisitAllPoints([[0, 0], [1, 1], [2, 2]]))
    print(solution.minTimeToVisitAllPoints([[0, 1], [2, 3], [4, 0]]))
