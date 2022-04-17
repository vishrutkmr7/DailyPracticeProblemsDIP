# This problem was recently asked by Microsoft:

# Given the root of a binary tree, print its level-order traversal.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_level_order(root):
    # Fill this in.
    if root is None:
        return
    queue = [root]
    while queue:
        print(queue[0].val, end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
