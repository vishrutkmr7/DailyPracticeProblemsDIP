# This problem was recently asked by Apple:

# Given a list of strings, find the list of characters that appear in all strings.


MAX_CHAR = 26


def common_characters(strs):
    # Fill this in.
    n = len(strs)
    res = []
    prim = [True] * MAX_CHAR
    for i in range(n):
        sec = [False] * MAX_CHAR

        for j in range(len(strs[i])):
            if prim[ord(strs[i][j]) - ord("a")]:
                sec[ord(strs[i][j]) - ord("a")] = True

        for i in range(MAX_CHAR):
            prim[i] = sec[i]

    for i in range(26):
        if prim[i]:
            res.append(chr(i + ord("a")))

    return res


print(common_characters(["google", "facebook", "youtube"]))
# ['e', 'o']
