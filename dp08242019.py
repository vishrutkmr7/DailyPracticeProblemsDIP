# This problem was recently asked by Google:

# There are n people lined up, and each have a height represented as an integer.
# A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to
# see what has happened. How many witnesses are there?

def witnesses(heights):
    # Fill this in.
    heights.reverse()
    n = len(heights)
    witnesses = []
    maxL = 0

    for i in range(0, n):
        if i == 0 or (heights[i] > maxL):
            witnesses.append(heights[i])
            maxL = heights[i]
    
    return len(witnesses)


print (witnesses([3, 6, 3, 4, 1]))
# 3
