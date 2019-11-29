#  This problem was recently asked by Uber:

# Given a postorder traversal for a binary search tree, reconstruct the tree.
# A postorder traversal is a traversal order where the left child always comes before the right child,
# and the right child always comes before the parent for all nodes.


INT_MIN = -2 ** 31
INT_MAX = 2 ** 31


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return (
            "("
            + str(self.value)
            + ", "
            + self.left.__repr__()
            + ", "
            + self.right.__repr__()
            + ")"
        )


def constructTreeUtil(post, postIndex, key, min, max, size):
    if postIndex[0] < 0:
        return None
    root = None
    if key > min and key < max:
        root = Node(key)
        postIndex[0] = postIndex[0] - 1

        if postIndex[0] >= 0:
            root.right = constructTreeUtil(
                post, postIndex, post[postIndex[0]], key, max, size
            )
            root.left = constructTreeUtil(
                post, postIndex, post[postIndex[0]], min, key, size
            )

    return root


def create_tree(postorder):
    # Fill this in.
    n = len(postorder)
    postIndex = [n - 1]
    return constructTreeUtil(
        postorder, postIndex, postorder[postIndex[0]], INT_MIN, INT_MAX, n
    )


# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))
# (2, (1, None, None), (3, None, None))
#     2
#    / \
#   1   3
