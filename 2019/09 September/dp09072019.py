# This problem was recently asked by Google:

# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    # Fill this in.
    deep = height(node)
    val = value(node, deep)
    return val, deep


def height(node):
    if not node:
        return 0

    l = height(node.left)
    r = height(node.right)
    return max(l, r) + 1


def value(root, levels):
    if not root:
        return
    if levels == 1:
        print(root)
        # return root
    elif levels > 1:
        value(root.left, levels - 1)
        value(root.right, levels - 1)


root = Node("a")
root.left = Node("b")
root.left.left = Node("d")
root.right = Node("c")
deep = height(root)
print(deepest(root))
# (d, 3)
