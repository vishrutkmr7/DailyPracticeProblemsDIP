#  This problem was recently asked by AirBNB:

# Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above it. Here's an example of the Pascal's Triangle of size 5.
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# Given an integer n, generate the n-th row of the Pascal's Triangle.


def pascal_triangle_row(n):
    # Fill this in.
    n = n - 1
    line = [1]

    for k in range(max(n, 0)):
        line.append(int(line[k] * (n - k) / (k + 1)))

    return line


print(pascal_triangle_row(6))
# [1, 5, 10, 10, 5, 1]
