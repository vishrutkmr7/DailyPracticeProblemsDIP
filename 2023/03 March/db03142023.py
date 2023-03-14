"""
You are given the root of a binary tree. Each node in the tree contains either a value of zero or a value of one.
Each path in the tree from root to leaf forms a binary string and therefore a decimal value.
Return the sum of all root to leaf paths using each path’s decimal value.
Note: It is guaranteed that the sum of all paths will fit in an integer value.

Ex: Given the following root…

     0
    / \
   1   1, return 2. (Our two paths are 01 and 01 which is 1 + 1 = 2).
Ex: Given the following root…

    1
   /  \
  1    0, return 5.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path = path * 2 + node.val
            if not node.left and not node.right:
                return path
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    print(solution.sumRootToLeaf(root))

    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    print(solution.sumRootToLeaf(root))
