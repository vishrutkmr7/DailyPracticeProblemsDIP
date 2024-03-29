# This problem was recently asked by Google:

# Given a node in a binary search tree (may not be the root), find the next largest node in the binary search tree
# (also known as an inorder successor). The nodes in this binary search tree will also have a parent field to traverse up the tree.


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"


def minValue(node):
    current = node
    while current is not None and current.left is not None:
        current = current.left

    return current.value


def inorder_successor(node):
    # Fill this in.
    if node.right is not None:
        return minValue(node.right)

    p = node.parent
    while p is not None and node == p.right:
        node = p
        p = p.parent
    return p.value


def insert(node, data):
    if node is None:
        return Node(data)
    if data <= node.data:
        temp = insert(node.left, data)
        node.left = temp
    else:
        temp = insert(node.right, data)
        node.right = temp
    temp.parent = node
    return node


tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right
#     3
#    / \
#   2   4
#  /     \
# 1       5
print(inorder_successor(tree.left))
# 3
print(inorder_successor(tree.right))
# 5
