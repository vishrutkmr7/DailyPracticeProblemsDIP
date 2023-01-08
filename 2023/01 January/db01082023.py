"""
A boring tree is a tree whose nodes only contain a single value. Given a reference to the root of a binary tree, root,
return whether or not it is a boring tree.
Note: It is guaranteed that a single value exists within the tree.

Ex: Given the following root…

       7
      / \
     7   7, return true.
Ex: Given the following root…

       1
      / \
     2   3, return false.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBoringTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.isBoringTree(root.left) and self.isBoringTree(root.right)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isBoringTree(TreeNode(7, TreeNode(7), TreeNode(7))))
    print(solution.isBoringTree(TreeNode(1, TreeNode(2), TreeNode(3))))
