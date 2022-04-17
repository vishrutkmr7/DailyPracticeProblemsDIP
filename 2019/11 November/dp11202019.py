# This problem was recently asked by Amazon:

# Given a binary tree and a given node value, return all of the node's cousins.
# Two nodes are considered cousins if they are on the same level of the tree with different parents.
# You can assume that all nodes will have their own unique value.


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def getLevel(root, node, level):
    if root is None:
        return 0
    if root.value == node:
        return level

    downlevel = getLevel(root.left, node, level + 1)
    if downlevel != 0:
        return downlevel

    return getLevel(root.right, node, level + 1)


lvlarr = []


def printGivenLevel(root, node, level):
    if root is None or level < 2:
        return
    if level == 2:
        if root.left == node or root.right == node:
            return
        if root.left:
            lvlarr.append(root.left.value)
        if root.right:
            lvlarr.append(root.right.value)

    elif level > 2:
        printGivenLevel(root.left, node, level - 1)
        printGivenLevel(root.right, node, level - 1)


class Solution(object):
    def list_cousins(self, tree, val):
        # Fill this in.
        level = getLevel(tree, val, 1)
        printGivenLevel(tree, val, level)
        result = filter(lambda x: x != val, lvlarr)
        return list(result)


#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, 5))
# [4, 6]
