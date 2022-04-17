# This problem was recently asked by Twitter:

# Given 2 strings s and t, find and return all indexes in string s where t is an anagram.


MAX = 256


def compare(arr1, arr2):
    return all(arr1[i] == arr2[i] for i in range(MAX))


def find_anagrams(s, t):
    # Fill this in.
    M = len(t)
    N = len(s)
    res = []
    countP = [0] * MAX
    countTW = [0] * MAX

    for i in range(M):
        (countP[ord(t[i])]) += 1
        (countTW[ord(s[i])]) += 1

    for i in range(M, N):
        if compare(countP, countTW):
            res.append(i - M)
        (countTW[ord(s[i])]) += 1
        (countTW[ord(s[i - M])]) -= 1

    if compare(countP, countTW):
        res.append(N - M)

    return res


print(find_anagrams("acdbacdacb", "abc"))
# [3, 7]
