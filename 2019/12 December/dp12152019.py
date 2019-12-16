# This problem was recently asked by Google:

# Given a binary tree, find and return the largest path from root to leaf.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_sum(tree):
    if not tree:
        return

    lb = 0 if tree.left is None else max_sum(tree.left)
    rb = 0 if tree.right is None else max_sum(tree.right)

    return lb + tree.value if lb > rb else rb + tree.value


resPath = []


def max_path(tree, sum):
    if sum == 0:
        return True

    if tree is None:
        return False

    left = max_path(tree.left, sum - tree.value)
    right = max_path(tree.right, sum - tree.value)

    if left or right:
        resPath.append(tree.value)

    return left or right


def largest_path_sum(tree):
    # Fill this in.
    maxSum = max_sum(tree)
    max_path(tree, maxSum)
    resPath.reverse()
    return resPath


tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
print(largest_path_sum(tree))
# [1, 3, 5]
