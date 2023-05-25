"""
Given the reference to a binary tree, return the total number of magic nodes in the tree.
Note: A node is magical if no value in the path from the root to the current node is greater
than the current node’s value.

Ex: Given the following binary tree…

      1
    /   \
   2     3, return 3 (all nodes are magic nodes)
Ex: Given the following binary tree…

      5
    /   \
   4     9
  / \
 8   7, return 4 (5, 8, 7, and 9 are all magic nodes).
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, curMax):
            if not node:
                return
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)

        count = [0]
        dfs(root, root.val)

        return count[0]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.goodNodes(root))  # 3

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(9)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(7)
    print(solution.goodNodes(root))  # 4
