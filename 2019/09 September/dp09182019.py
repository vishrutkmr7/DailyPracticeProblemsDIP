# This problem was recently asked by Twitter:

# You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary search tree.


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


res = []


def largestBST(root):
    largest_bst_subtree(root)
    return getValue(res)


def largest_bst_subtree(root):
    # Fill this in.
    if (root is None) or (root.left is None and root.right is None):
        return root

    l = largest_bst_subtree(root.left)
    r = largest_bst_subtree(root.right)

    if isBST(root):
        p = {"tree": root, "size": size(root)}
        res.append(p)


def isBST(root, l=None, r=None):
    if root is None:
        return True
    if l != None and root.key <= l.key:
        return False
    if r != None and root.key >= r.key:
        return False
    return isBST(root.left, l, root) and isBST(root.right, root, r)


def size(node):
    return 0 if node is None else size(node.left) + 1 + size(node.right)


def getValue(result):
    ans = sorted(result, key=lambda i: i["size"], reverse=True)
    return ans[0]["tree"]


#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largestBST(node))
# 749
