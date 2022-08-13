# This problem was recently asked by Facebook:

# Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

def findSequence(seq):
    # Fill this in.
    i = 0
    j = -1
    maxLen = 0

    for k in range(1, len(seq)):
        if seq[k] == seq[k - 1]:
            continue

        if j >= 0 and seq[j] != seq[k]:
            maxLen = max(k - i, maxLen)
            i = j + 1

        j = k - 1

    return max(len(seq) - i, maxLen)


print (findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4