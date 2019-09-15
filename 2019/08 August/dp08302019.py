# This problem was recently asked by Microsoft:

# You are given an array of intervals - that is, an array of tuples (start, end).
# The array may not be sorted, and could contain overlapping intervals.Return another array where the overlapping intervals are merged.

def merge(intervals):
    # Fill this in.
    saved = list(intervals[0])
    temp = []
    for i, j in sorted([sorted(t) for t in intervals]):
        if i <= saved[1]:
            saved[1] = max(saved[1], j)
        else:
            temp.append(tuple(saved))
            saved[0] = i
            saved[1] = j
    temp.append(tuple(saved))
    return temp
  
print (merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
