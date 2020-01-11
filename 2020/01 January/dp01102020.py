# This problem was recently asked by LinkedIn:

# Given a list of points as a tuple (x, y) and an integer k, find the k closest points to the origin (0, 0).

import math


def distanceFromOrigin(point):
    return math.sqrt((point[0] * point[0]) + (point[1] * point[1]))


def closest_points(points, k):
    # Fill this in.
    distArr = []
    for point in points:
        distArr.append(distanceFromOrigin(point))

    minIndices = sorted(range(len(distArr)), key=lambda sub: distArr[sub])[:k]
    res = []
    for index in minIndices:
        res.append(points[index])

    return res


print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
# [(1, 2), (0, 0)]
