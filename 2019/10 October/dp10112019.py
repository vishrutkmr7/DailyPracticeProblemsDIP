# This problem was recently asked by Microsoft:

# A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree
# is the same as the right side of the tree.
# Given a k-ary tree, figure out if the tree is symmetrical.


class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


def is_symmetric(root):
    # Fill this in.
    mirror = Mirror(root)
    if root == mirror:
        return True
    else:
        return False


def Mirror(root):
    if root is None:
        return

    n = len(root.children)
    if n < 2:
        return

    for i in range(n):
        Mirror(root.children[i])
    root.children.reverse()
    return root


tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True
