# This problem was recently asked by Google:

# You are given a stream of numbers. Compute the median for each new element .


def running_median(stream):
    # Fill this in.
    temp = []
    for i in stream:
        temp.append(i)
        median(temp)


def median(stream):
    n = len(stream)
    stream.sort()
    if n % 2 == 0:
        p = stream[int(n / 2)]
        q = stream[int(n / 2) - 1]
        print((p + q) / 2)
    else:
        print(stream[int((n / 2) - 0.5)])


running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2
