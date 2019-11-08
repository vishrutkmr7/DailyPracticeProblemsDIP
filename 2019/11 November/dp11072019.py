# This problem was recently asked by Microsoft:

# Return the longest run of 1s for a given integer n's binary representation.


def longest_run(n):
    # Fill this in.
    nBin = str(bin(n).replace("0b", ""))
    binList = list(nBin.split("0"))
    maxAns = []
    for i in binList:
        maxAns.append(len(i))

    return max(maxAns)


print(longest_run(242))
# 4
