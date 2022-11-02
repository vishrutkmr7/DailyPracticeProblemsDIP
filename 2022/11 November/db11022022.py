"""
You are given the reference to the root of a binary tree and are asked to trim the tree of
“dead” nodes. A dead node is a node whose value is listed in the provided dead array.
Once the tree has been trimmed of all dead nodes, return a list containing references
to the roots of all the remaining segments of the tree.

Ex: Given the following binary tree and array dead…

      3
    /   \
   1     7
 /  \   /  \
2    8 4    6, dead = [7, 8], return a list containing a reference to the following nodes [3, 4, 6].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        print(self.val)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()


class Solution:
    def trimTree(self, root, dead):
        if not root:
            return None
        root.left = self.trimTree(root.left, dead)
        root.right = self.trimTree(root.right, dead)
        return root.left or root.right or None if root.val in dead else root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    root.printTree()
    print(solution.trimTree(root, [7, 8]).printTree())
