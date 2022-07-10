"""
Given a binary tree, return its maximum depth.
Note: the maximum depth is defined as the number of nodes
along the longest path from root node to leaf node.

Ex: Given the following tree…

    9
   / \
  1   2
return 2
Ex: Given the following tree…

    5
   / \
  1  29
    /  \
   4   13
return 3
"""


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinaryTree(value)
        elif self.right:
            self.right.insert(value)
        else:
            self.right = BinaryTree(value)


def maxDepth(root):
    if root is None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1


# Test cases
tree = BinaryTree(9)
tree.insert(1)
tree.insert(2)
print(maxDepth(tree))

tree = BinaryTree(5)
tree.insert(1)
tree.insert(29)
tree.insert(4)
tree.insert(13)
print(maxDepth(tree))
