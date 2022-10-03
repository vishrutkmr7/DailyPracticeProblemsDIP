"""
This question is asked by Facebook.
Given an undirected graph determine whether it is bipartite.
Note: A bipartite graph, also called a bigraph, is a set of graph vertices decomposed into
two disjoint sets such that no two graph vertices within the same set are adjacent.

Ex: Given the following graph...

graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
0----1
|    |
|    |
3----2
return true.
Ex: Given the following graph...

graph = [[1, 2], [0, 2, 3], [0, 1, 3], [0, 2]]
0----1
|  / |
| /  |
3----2
return false.
"""


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        colors = {}
        for node in range(len(graph)):
            if node not in colors:
                colors[node] = 0
                queue = [node]
                while queue:
                    node = queue.pop(0)
                    for neighbor in graph[node]:
                        if neighbor not in colors:
                            colors[neighbor] = colors[node] ^ 1
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[node]:
                            return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True
    assert solution.isBipartite([[1, 2], [0, 2, 3], [0, 1, 3], [0, 2]]) is False
    print("All tests passed.")
