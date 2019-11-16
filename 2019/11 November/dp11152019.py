# This problem was recently asked by AirBNB:

# We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we cannot run the same task simultaneously.

# Given a list of tasks, find how long it will take to complete the tasks in the order they are input.


def findTime(arr, cooldown):
    # Fill this in.
    resArr = []
    n = len(arr)


print(findTime([1, 1, 2, 1], 2))
# 7
