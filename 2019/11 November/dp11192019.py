#  This problem was recently asked by Facebook:

# Given a list of building in the form of (left, right, height), return what the skyline should look like.
# The skyline should be in the form of a list of (x-axis, height),
# where x-axis is the next point where there is a change in height starting from 0,
# and height is the new height starting from the x-axis.


def generate_skyline(buildings):
    # Fill this in.
    if not buildings:
        return []
    if len(buildings) == 1:
        l, r, h = buildings[0]
        return [[l, h], [r, 0]]

    mid = len(buildings) // 2
    left = generate_skyline(buildings[:mid])
    right = generate_skyline(buildings[mid:])
    return merge(left, right)


def merge(left, right):
    h1, h2 = 0, 0
    i, j = 0, 0
    result = [[0, 0]]
    while i < len(left) and j < len(right):
        x0 = left[i][0]
        x1 = right[j][0]
        if x0 <= x1:
            h1 = left[i][1]
            i += 1
        if x1 <= x0:
            h2 = right[j][1]
            j += 1
        if max(h1, h2) != result[-1][1]:
            result.append([min(x0, x1), max(h1, h2)])
    result.extend(right[j:])
    result.extend(left[i:])
    return result[1:]


#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]
