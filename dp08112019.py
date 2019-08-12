# This problem was recently asked by LinkedIn:

# You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time.
# Write a function that returns the number of unique ways to climb the stairs.
# Can you find a solution in O(n) time?

def staircase(n):
    # Fill this in.
    X = [1, 2] #Steps at a time
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)
        cache[i] += 1 if i in X else 0
    return cache[-1]
    
print (staircase(4))
# 5
print (staircase(5))
# 8