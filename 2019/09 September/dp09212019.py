#  This problem was recently asked by AirBNB:

# Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).


from collections import defaultdict


def groupAnagramWords(strs):
    # Fill this in.
    temp = defaultdict(list)
    for ele in strs:
        temp[str(sorted(ele))].append(ele)
    res = list(temp.values())

    return res


print(groupAnagramWords(["abc", "bcd", "cba", "cbd", "efg"]))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
