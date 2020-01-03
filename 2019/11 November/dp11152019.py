# This problem was recently asked by AirBNB:

# We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we cannot run the same task simultaneously.
# Given a list of tasks, find how long it will take to complete the tasks in the order they are input.


def findTime(arr, cooldown):
    # Fill this in.
    n = len(arr)
    if cooldown <= 0 or n == 0:
        return n

    curr = ""
    pre = arr[0]
    count = 1
    for i in range(1, n):
        curr = arr[i]
        if curr == pre:
            count += cooldown
        count += 1
        pre = curr

    return count + 1


print(findTime([1, 1, 2, 1], 2))
# 7

# Solution: 01/02/2020: Amazon: Schedule Tasks
print(findTime(["q", "q", "s", "q", "w", "w"], 4))
# 6
