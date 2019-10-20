# This problem was recently asked by Facebook:

# You are given the root of a binary tree. Find the path between 2 nodes that maximizes the sum of all the nodes in the path,
# and return the sum. The path does not necessarily need to go through the root.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maxPathSumUtil(root):
    # Fill this in.
    if root is None:
        return 0

    l = maxPathSumUtil(root.left)
    r = maxPathSumUtil(root.right)
    max_single = max(max(l, r) + root.val, root.val)
    max_top = max(max_single, l + r + root.val)
    maxPathSumUtil.res = max(maxPathSumUtil.res, max_top)
    return max_single


def maxPathSum(root):
    maxPathSumUtil.res = float("-inf")
    maxPathSumUtil(root)
    return maxPathSumUtil.res


# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxPathSum(root))
# 42
