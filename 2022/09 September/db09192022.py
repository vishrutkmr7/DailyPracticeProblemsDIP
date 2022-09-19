"""
Given the reference to the root of a binary tree and a value k,
return the number of paths in the tree such that the sum of the nodes along the path equals k.
Note: The path does not need to start at the root of the tree, but must move downward.

Ex: Given the following binary tree and value k…

      3
     / \
    1   8
k = 11, return 1 (3 -> 8).
Ex: Given the following binary tree and value k…

      2
     / \
   -4   9
   /
  2
k = 2, return 3 (2, 2 -> -4, -4 -> 2).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, k: int) -> int:
        return (
            self.pathSumFrom(root, k)
            + self.pathSum(root.left, k)
            + self.pathSum(root.right, k)
            if root
            else 0
        )

    def pathSumFrom(self, node: TreeNode, k: int) -> int:
        return (
            (node.val == k)
            + self.pathSumFrom(node.left, k - node.val)
            + self.pathSumFrom(node.right, k - node.val)
            if node
            else 0
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.pathSum(TreeNode(3, TreeNode(1), TreeNode(8)), 11))
    print(solution.pathSum(TreeNode(2, TreeNode(-4, TreeNode(2)), TreeNode(9)), 2))
