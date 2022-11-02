"""
Given a list of points, return the k closest points to the origin (0, 0).

Ex: Given the following points and value of k…

points = [[1, 1],[-2, -2]], k = 1, return [[1, 1]].
"""


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.kClosest([[1, 1], [-2, -2]], 1))
