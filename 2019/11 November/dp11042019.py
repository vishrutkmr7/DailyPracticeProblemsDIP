# This problem was recently asked by Facebook:

# Given a directed graph, reverse the directed graph so all directed edges are reversed.
# Input:
# A -> B, B -> C, A -> C
# Output:
# B -> A, C -> B, C -> A

from collections import defaultdict


class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value


def reverse_graph(graph):
    # Fill this in.
    revG = {}
    for val, node in graph.items():
        adj = []
        for j in node.adjacent:
            adj.append(j.value)

        for it in graph:
            if it not in revG.keys():
                revG[it] = Node(it)
            if it in adj:
                revG[it].adjacent.append(val)

    return revG


a = Node("a")
b = Node("b")
c = Node("c")

a.adjacent += [b, c]
b.adjacent += [c]

graph = {a.value: a, b.value: b, c.value: c}

for _, val in reverse_graph(graph).items():
    print(_, val.adjacent)
# a []
# b ['a']
# c ['a', 'b']
