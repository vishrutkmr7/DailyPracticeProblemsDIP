"""
Given a binary tree, return a list containing its in-order traversal without using recursion.

Ex: Given the following tree…

      2     
     / \   
    1   3
return [1, 2, 3]
Ex: Given the following tree…

        2
       / \
      1   7
     / \
    4   8
return [4, 1, 8, 2, 7]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


# Test Cases
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
s = Solution()
print(s.inorderTraversal(root))  # returns [1, 2, 3]

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
s = Solution()
print(s.inorderTraversal(root))  # returns [4, 1, 8, 2, 7]
