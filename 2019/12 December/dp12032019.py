# This problem was recently asked by Facebook:

# Given a list of words, for each word find the shortest unique prefix.
# You can assume a word will not be a substring of another word (ie play and playing won't be in the same words list)


class TrieNode:
    def __init__(self, freq=None):
        self.child = None
        self.freq = freq


def insert(root, string):
    l = len(string)
    temp = root

    for lvl in range(0, l):
        index = string[lvl]
        if temp.child != index:
            temp.child = TrieNode(index)
        else:
            temp.child.freq += 1
        temp = temp.child


def findPrefixesUtil(root, prefix, n):
    if root is None:
        return

    if root.freq == 1:
        prefix[n] = ""
        return

    for i in range(0, n):
        if root.child is not None:
            prefix[n] = i
            findPrefixesUtil(root.child[i], prefix, n + 1)


def shortest_unique_prefix(words):
    # Fill this in.
    n = len(words)
    root = TrieNode()
    root.freq = 0
    for i in range(0, n):
        insert(root, words[i])

    prefix = []
    findPrefixesUtil(root, prefix, 0)


print(shortest_unique_prefix(["joma", "john", "jack", "techlead"]))
# ['jom', 'joh', 'ja', 't']

