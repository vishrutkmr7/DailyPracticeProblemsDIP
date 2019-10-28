# This problem was recently asked by Apple:

# You are given the root of a binary tree, along with two nodes, A and B. Find and return the lowest common ancestor of A and B.
# For this problem, you can assume that each node also has a pointer to its parent, along with its left and right child.


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def lowestCommonAncestor(root, a, b):
    # Fill this in.
    while root:
        if root.val > a and root.val > b:
            root = root.left
        elif root.val < a and root.val < b:
            root = root.right

        else:
            break

    return root.parent


#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.right.left = TreeNode("d")
root.right.right = TreeNode("e")
root.left.parent = root
root.right.parent = root
root.right.left.parent = root.right
root.right.right.parent = root.right
a = "d"
b = "e"

print(lowestCommonAncestor(root, a, b).val)
# c
