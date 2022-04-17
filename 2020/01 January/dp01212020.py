# This problem was recently asked by Apple:

# Given a list of strings, find the list of characters that appear in all strings.


MAX_CHAR = 26


def common_characters(strs):
    prim = [True] * MAX_CHAR
    n = len(strs)
    for i in range(n):
        sec = [False] * MAX_CHAR

        for j in range(len(strs[i])):
            if prim[ord(strs[i][j]) - ord("a")]:
                sec[ord(strs[i][j]) - ord("a")] = True

        for i in range(MAX_CHAR):
            prim[i] = sec[i]

    return [chr(i + ord("a")) for i in range(26) if prim[i]]


print(common_characters(["google", "facebook", "youtube"]))
# ['e', 'o']
