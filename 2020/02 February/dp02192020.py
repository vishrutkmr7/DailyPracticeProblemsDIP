# This problem was recently asked by Amazon:

# A number can be constructed by a path from the root to a leaf. Given a binary tree, sum all the numbers that can be constructed from the root to all leaves.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def treePathsSumUtil(root, val):
    # Fill this in.
    if root is None:
        return 0

    # Update val
    val = val * 10 + root.value

    # If current node is leaf, return the current value of val
    if root.left is None and root.right is None:
        return val

    # Recur sum of values for left and right subtree
    return treePathsSumUtil(root.left, val) + treePathsSumUtil(root.right, val)


def bst_numbers_sum(root):
    return treePathsSumUtil(root, 0)


n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5

print(bst_numbers_sum(n1))
# 262
# Explanation: 124 + 125 + 13 = 262
