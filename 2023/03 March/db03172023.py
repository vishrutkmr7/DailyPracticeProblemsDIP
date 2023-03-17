"""
Given the reference to the root of a binary search tree and two values,
low and high, update the tree such that any nodes containing values that
are strictly outside low and high are removed.

Ex: Given the following root, low, and high...

root = 1
      / \
     2   3, low = 1, high = 2, return the tree updated as follows...
       1
      /
     2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    low = 1
    high = 2
    print(solution.trimBST(root, low, high))
