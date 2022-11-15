"""
Given a binary tree, count the total number of nodes it contains.

Ex: Given the following binary tree...

         1
        / \
       2   3, return 3.
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left, right, l, r = root.left, root.right, 1, 1
        while left:
            left, l = left.left, l + 1
        while right:
            right, r = right.right, r + 1

        if l == r:
            return 2**l - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.countNodes(TreeNode(1, TreeNode(2), TreeNode(3))))
