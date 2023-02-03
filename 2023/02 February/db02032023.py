"""Given the root of two binary trees, a and b, return the resulting tree when you overlay a on top of b.
Note: For any nodes that overlap a is placed on top of b, the resulting tree’s node should
contain their sum.

Ex: Given the following a and b…

a = 1     b = 4
   / \       / \
  2   3     5   6, return the resulting tree...
           5 (1 + 4)
         /   \
(2 + 5) 7     9 (3 + 6)
Ex: Given the following a and b…

a = 7     b = 9
   / \       /
  2   1     5, return the resulting tree...
         16
        /  \
       7    1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    # Example 1
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    b = TreeNode(4)
    b.left = TreeNode(5)
    b.right = TreeNode(6)
    print(solution.mergeTrees(a, b))

    # Example 2
    a = TreeNode(7)
    a.left = TreeNode(2)
    a.right = TreeNode(1)
    b = TreeNode(9)
    b.left = TreeNode(5)
    print(solution.mergeTrees(a, b))
