# This problem was recently asked by Twitter:

# You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that value.


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def minimum_level_sum(root):
    # Fill this in.
    if root is None:
        return
    result = root.val
    q = []
    q.append(root)

    while len(q) != 0:
        s = 0
        while len(q) != 0:
            temp = q[0]
            q = []
            s = s + temp.val

            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)

        result = min(s, result)

    # return result


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)
node.left.left.left = node.left.left.right = None
node.left.right.left = node.left.right.right = None
node.right.left = None
node.right.right.left = node.right.right.right = None


print(minimum_level_sum(node))
# 7
