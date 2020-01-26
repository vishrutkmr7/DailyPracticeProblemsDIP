# This problem was recently asked by Uber:

# Given a string s and a character c, find the distance for all characters in the string to the character c in the string s.
# You can assume that the character c will appear at least once in the string.


def shortest_dist(S, X):
    # Fill this in.
    prev = float("-inf")
    ans = []
    for i, j in enumerate(S):
        if j == X:
            prev = i
        ans.append(i - prev)

    prev = float("inf")
    for i in range(len(S) - 1, -1, -1):
        if S[i] == X:
            prev = i
        ans[i] = min(ans[i], prev - i)

    return ans


print(shortest_dist("helloworld", "l"))
# [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
