# This problem was recently asked by Microsoft:

# You 2 integers n and m representing an n by m grid,
# determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

def num_ways(n, m):
    # Fill this in.
    return 1 if m == 1 or n == 1 else num_ways(m-1, n) + num_ways(m, n-1)

print (num_ways(2, 2))
# 2
