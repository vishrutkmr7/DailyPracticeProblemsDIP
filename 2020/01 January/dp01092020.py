# This problem was recently asked by Twitter:

# Given a binary search tree (BST) and a value s, split the BST into 2 trees, where one tree has all values less than or equal to s,
# and the other tree has all values greater than s while maintaining the tree structure of the original BST.
# You can assume that s will be one of the node's value in the BST. Return both tree's root node as a tuple.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left:
            if self.right:
                return f"({self.value}, {self.left}, {self.right})"
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"


def setChild(node, toLeft, child):
    if toLeft:
        node.left = child
    else:
        node.right = child


def split_bst(bst, s):
    # Fill this in.
    root2 = None
    parent1 = None
    parent2 = None
    toLeft = bst.value is not None and s < bst.value

    while bst.value is not None:
        while bst.value is not None and (s < bst.value == toLeft):
            parent1 = bst
            bst = bst.left if toLeft else bst.right

        if parent1 is not None:
            setChild(parent1, toLeft, None)

        toLeft = not toLeft  # toggle
        if root2 is None:
            root2 = bst
        elif parent2 is not None:
            setChild(parent2, toLeft, bst)

        parent2 = parent1
        parent1 = None

    return root2


n2 = Node(2)
n1 = Node(1, None, n2)

n5 = Node(5)
n4 = Node(4, None, n5)

root = Node(3, n1, n4)

print(root)
# (3, (1, (2)), (4, None, (5)))
# How the tree looks like
#     3
#   /   \
#  1     4
#   \     \
#    2     5

print(split_bst(root, 2))
# ((1, None, (2)), (3, None, (4, None, (5))))
# Split into two trees
# 1    And   3
#  \          \
#   2          4
#               \
#                5
