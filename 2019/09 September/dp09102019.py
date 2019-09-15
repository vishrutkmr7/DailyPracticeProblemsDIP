# This problem was recently asked by Facebook:

# You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise.
# Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root
# and all values in the right subtree are greater than or equal to the root.

INT_MAX = 4294967296
INT_MIN = -4294967296


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def is_bst(root):
    # Fill this in.
    return is_bst_util(root, INT_MIN, INT_MAX)


def is_bst_util(root, minv, maxv):
    if root is None:
        return True  # Empty tree is also a BST

    if root.key < minv or root.key > maxv:
        return False  # Min/Max constraint

    return (is_bst_util(root.left, minv, root.key - 1)) and (
        is_bst_util(root.right, root.key + 1, maxv)
    )


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
# 1  4 6
