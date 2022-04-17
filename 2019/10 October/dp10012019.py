#  This problem was recently asked by Apple:

# You are given the root of a binary tree. You need to implement 2 functions:

# 1. serialize(root) which serializes the tree into a string representation
# 2. deserialize(s) which deserializes the string back to the original tree that it represents

# For this problem, often you will be asked to design your own serialization format.
# However, for simplicity, let's use the pre-order traversal of the tree.

import collections


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        result = "" + str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


serial = ""


def serialize(root):
    # Fill this in.
    global serial
    if root is None:
        serial += "# "
        # return serial
        return
    serial += f"{str(root.val)} "
    serialize(root.left)
    serialize(root.right)

    return serial


def deserialize(data):
    # Fill this in.
    def decode(vals):
        val = next(vals)
        if val == "#":
            return None
        node = Node(int(val))
        node.left = decode(vals)
        node.right = decode(vals)
        return node

    vals = iter(data.split())
    return decode(vals)


#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize("1 3 2 # # 5 # # 4 # 7 # #"))
# 132547
