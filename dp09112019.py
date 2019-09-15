# This problem was recently asked by Amazon:

# Given a binary tree, return all values given a certain height h.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


ans = []


def findValues(root, height):
    if root is None:
        return
    if height == 0 or height == 1:
        ans.append(root.value)
    else:
        valuesAtHeight(root.left, height - 1)
        valuesAtHeight(root.right, height - 1)


def valuesAtHeight(root, height):
    # Fill this in.
    findValues(root, height)
    return ans


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]
