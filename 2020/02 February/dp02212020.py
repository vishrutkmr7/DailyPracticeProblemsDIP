# This problem was recently asked by Microsoft:

# Given a node in a connected directional graph, create a copy of it.


class Node:
    def __init__(self, value, adj=None):
        self.value = value
        self.adj = adj

        # Variable to help print graph
        self._print_visited = set()
        if self.adj is None:
            self.adj = []

    # Able to print graph
    def __repr__(self):
        if self in self._print_visited:
            return ""
        self._print_visited.add(self)
        final_str = "".join(f"{n}\n" for n in self.adj)
        self._print_visited.remove(self)
        return f"{final_str}({self.value}, ({[n.value for n in self.adj]}))"


def deep_copy_graph(graph_node, visited=None):
    # Fill this in.
    return graph_node


n5 = Node(5)
n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2)
n1 = Node(1, [n5])
n5.adj = [n3]
n4.adj = [n3, n2]
n2.adj = [n4]
graph_copy = deep_copy_graph(n1)
print(graph_copy)
# (2, ([4]))
# (4, ([3, 2]))
# (3, ([4]))
# (5, ([3]))
# (1, ([5]))
