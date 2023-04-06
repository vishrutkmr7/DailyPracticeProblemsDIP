"""
Given the reference to the root of a binary tree, and a target value,
remove all the leaf nodes that contain the target and return the modified tree.
Note: If you remove a leaf node that contains the target value and the parent node
now becomes a leaf with a value of target, you must remove the parent as well. 

Ex: Given the following binary tree and target…

      1
     / \
    2   3
   /
  2, target = 2, return the tree modified as follows...
       1
        \
         3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.val == target and not root.left and not root.right:
            return None
        return root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3))
    target = 2
    print(solution.removeLeafNodes(root, target))
