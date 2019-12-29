# This problem was recently asked by Google:

# Given a positive integer, find the square root of the integer without using any built in square root or power functions
# (math.sqrt or the ** operator). Give accuracy up to 3 decimal points.


def sqrt(x):
    # Fill this in.
    start = 0
    end = x
    m = 0
    min_range = 0.0000000001

    while end - start > min_range:
        m = (start + end) / 2.0
        pow2 = m * m
        if abs(pow2 - x) <= min_range:
            return m
        elif pow2 < x:
            start = m
        else:
            end = m

        # print(m, ",", round(m, 3))

    return round(m, 3)


print(sqrt(5))
# 2.236
