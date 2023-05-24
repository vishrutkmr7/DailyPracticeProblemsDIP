"""
You are given an integer N, that represents N vertices (labeled zero to N - 1) that exist within
an acyclic graph. You are also given a list of edges where edges[i] contains two values: the source
node and the node that it connects to (i.e. to and from values). Return the smallest list of
required vertices such that you can reach every vertex in the graph. 
Note: You may assume only a single solution exists. 

Ex: Given the following N and edges…

N = 3, edges = [[0, 1], [1, 2]], return [0] (you only need to be able to access vertex zero to
reach every other node in the graph).
Ex: Given the following N and edges…

N = 4, edges = [[3, 1], [1, 2], [0, 2]], return [0, 3].
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


class Solution:
    def findSmallestVertex(self, n, edges):
        # Time O(N + E) || Space O(N)
        if not edges:
            return [0]

        graph = {i: Node(i) for i in range(n)}
        for edge in edges:
            graph[edge[0]].add_neighbor(graph[edge[1]])

        visited = set()
        result = []
        for node, value in graph.items():
            if node not in visited:
                self.dfs(value, visited, result)

        return result

    def dfs(self, node, visited, result):
        if node.val in visited:
            return

        visited.add(node.val)
        for neighbor in node.neighbors:
            self.dfs(neighbor, visited, result)

        result.append(node.val)


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.findSmallestVertex(3, [[0, 1], [1, 2]]))  # [0]
    print(sol.findSmallestVertex(4, [[3, 1], [1, 2], [0, 2]]))  # [0, 3]
