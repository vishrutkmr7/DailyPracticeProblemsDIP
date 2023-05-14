"""
Given two integer arrays, preorder and inorder, that represent the preorder and inorder traversal
of the same binary tree respectively, construct and return the binary tree that they represent.
Note: Both preorder and inorder consist of unique values.

Ex: Given the following preorder and inorder…

preorder = [1, 2, 3], inorder = [2, 1, 3], return the reference to a binary tree that looks as
follows...
        1
      /   \
     2     3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1 :], inorder[i + 1 :])
        return root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = solution.buildTree([1, 2, 3], [2, 1, 3])
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right is None
    print("Passed all tests!")
