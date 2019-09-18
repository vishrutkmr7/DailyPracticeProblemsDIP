# This problem was recently asked by Apple:

# Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.


def isSorted(words, order):
    # Fill this in.
    oIndex = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        for k in range(min(len(word1), len(word2))):
            if word1[k] != word2[k]:
                if oIndex[word1[k]] > oIndex[word2[k]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False

    return True


print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))
# True
