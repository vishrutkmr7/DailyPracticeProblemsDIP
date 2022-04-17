# This problem was recently asked by Microsoft:

# Return the longest run of 1s for a given integer n's binary representation.


def longest_run(n):
    # Fill this in.
    nBin = bin(n).replace("0b", "")
    binList = list(nBin.split("0"))
    maxAns = [len(i) for i in binList]
    return max(maxAns)


print(longest_run(242))
# 4
