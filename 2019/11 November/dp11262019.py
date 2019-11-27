# This problem was recently asked by Twitter:

# Given a tree, find if the binary tree is height balanced or not.
# A height balanced binary tree is a tree where every node's 2 subtree do not differ in height by more than 1.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def is_height_balanced(tree):
    # Fill this in.
    if tree is None:
        return True

    lh = height(tree.left)
    rh = height(tree.right)

    if (
        (abs(lh - rh) <= 1)
        and is_height_balanced(tree.left) is True
        and is_height_balanced(tree.right) is True
    ):
        return True

    return False


#     1
#    / \
#   2   3
#  /
# 4
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    /
#   2
#  /
# 4
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
