# This problem was recently asked by Apple:

# Given a list of points, an interger k, and a point p, find the k closest points to p.

import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def calculateDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def closest_points(points, k, p):
    # Fill this in.
    res = []
    distDict = {}
    for pt in points:
        dest = (pt.x, pt.y)
        dist = calculateDistance(pt.x, pt.y, p.x, p.y)
        distDict[dest] = dist

    for _ in range(k):
        min_key = min(distDict.keys(), key=lambda k: distDict[k])
        res.append(min_key)
        del distDict[min_key]

    return res


points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)]
print(closest_points(points, 2, Point(0, 2)))
# [(0, 0), (1, 1)]
