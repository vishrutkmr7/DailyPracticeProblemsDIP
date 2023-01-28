"""
Given a binary tree, invert it and return the resulting tree. 

Ex: Given the following binary tree…

        1
       /  \
      2    3, return...
         1
        /  \
       3    2
Ex: Given the following binary tree…

        1
       /  \
      2     3
     / \   /  \
    4   5 6    7, return...
         1
        /  \
       3     2
     /   \  /  \
    7    6 5    4 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
    )
    print(solution.invertTree(root))
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(solution.invertTree(root))
