# This problem was recently asked by Facebook:

# Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.

# Given a list of words, determine if there is a way to 'chain' all the words in a circle.
# Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
# Output: True
# Explanation:
# The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.

from collections import defaultdict

CHARS = 26
# Eulerian Graph problem
class Graph(object):
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = [[] for x in range(V)]  # a dynamic array
        self.inp = [0] * V

    # function to add an edge to graph
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.inp[w] += 1

    # Method to check if this graph is Eulerian or not
    def isSC(self):
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * self.V

        # Find the first vertex with non-zero degree
        n = 0
        for n in range(self.V):
            if len(self.adj[n]) > 0:
                break

        # Do DFS traversal starting from first non zero degree vertex.
        self.DFSUtil(n, visited)

        # If DFS traversal doesn't visit all vertices, then return false.
        for i in range(self.V):
            if len(self.adj[i]) > 0 and visited[i] == False:
                return False

        # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        for i in range(self.V):
            visited[i] = False

        # Do DFS for reversed graph starting from first vertex.
        # Staring Vertex must be same starting point of first DFS
        gr.DFSUtil(n, visited)

        # If all vertices are not visited in second DFS, then
        # return false
        for i in range(self.V):
            if len(self.adj[i]) > 0 and visited[i] == False:
                return False

        return True

    # This function returns true if the directed graph has an eulerian
    # cycle, otherwise returns false
    def isEulerianCycle(self):

        # Check if all non-zero degree vertices are connected
        if self.isSC() == False:
            return False

        # Check if in degree and out degree of every vertex is same
        for i in range(self.V):
            if len(self.adj[i]) != self.inp[i]:
                return False

        return True

    # A recursive function to do DFS starting from v
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in range(len(self.adj[v])):
            if not visited[self.adj[v][i]]:
                self.DFSUtil(self.adj[v][i], visited)

    # Function that returns reverse (or transpose) of this graph
    # This function is needed in isSC()
    def getTranspose(self):
        g = Graph(self.V)
        for v in range(self.V):
            # Recur for all the vertices adjacent to this vertex
            for i in range(len(self.adj[v])):
                g.adj[self.adj[v][i]].append(v)
                g.inp[v] += 1
        return g


def chainedWords(words):
    # Fill this in.
    n = len(words)
    g = Graph(CHARS)
    for i in range(n):
        s = words[i]
        g.addEdge(ord(s[0]) - ord("a"), ord(s[len(s) - 1]) - ord("a"))

    return g.isEulerianCycle()


print(chainedWords(["apple", "eggs", "snack", "karat", "tuna"]))
# True
