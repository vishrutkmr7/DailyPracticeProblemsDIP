# This problem was recently asked by Google:

# You are given an array of tuples (start, end) representing time intervals for lectures.
# The intervals may be overlapping. Return the number of rooms that are required.


def rooms(arr):
    # Fill this in.
    inTime = [x[0] for x in arr]
    outTime = [x[1] for x in arr]
    n = len(arr)
    inTime.sort()
    outTime.sort()
    nRooms = 1
    result = 1
    i = 1
    j = 0
    while i < n and j < n:
        if inTime[i] < outTime[j]:
            nRooms += 1
            i += 1
            if nRooms > result:
                result = nRooms
        else:
            nRooms -= 1
            j += 1

    return result


print(rooms([(30, 75), (0, 50), (60, 150)]))
# 2
