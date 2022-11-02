"""Given the reference to a binary tree, return the maximum path sum.
Note: The path that creates the maximum sum does not need to pass through the root of the tree.

Ex: Given the reference to the following binary tree...

     1
    / \
   4   9, return 14.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float("-inf")
        self.find_max_sum(root)
        return self.max_sum

    def find_max_sum(self, node):
        if not node:
            return 0

        left = max(self.find_max_sum(node.left), 0)
        right = max(self.find_max_sum(node.right), 0)

        self.max_sum = max(self.max_sum, node.val + left + right)

        return node.val + max(left, right)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPathSum(TreeNode(1, TreeNode(4), TreeNode(9))))
