# This problem was recently asked by Apple:

# Given a list of undirected edges which represents a graph, find out the number of connected components.


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


g = Graph(6)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(3, 0)
g.addEdge(4, 5)
cc = g.connectedComponents()
print(len(cc))
# 2
