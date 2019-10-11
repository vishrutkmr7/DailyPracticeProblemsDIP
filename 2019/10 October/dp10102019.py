# This problem was recently asked by Amazon:

# The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar.
# The definition of the h-index is if a scholar has at least h of their papers cited h times.


def hIndex(publications):
    # Fill this in.
    n = len(publications)
    eq = [0] * (n + 1)
    for h in range(n):
        if publications[h] >= n:
            eq[n] += 1
        else:
            eq[publications[h]] += 1

    s = 0
    for h in range(n, 0, -1):
        s += eq[h]
        if s >= h:
            return h

    return 0


print(hIndex([5, 3, 3, 1, 0]))
# 3
