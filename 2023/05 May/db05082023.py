"""
Given the root of a non-empty binary tree, return the length of the longest zigzag path.
Note: A zigzag path is a path that begins at any node in the tree and alternates between
moving left and moving right down the tree. It is guaranteed that the root you’re given
is not null.

Ex: Given the following root…

       1
     /   \
    3     4
         /
        8, return 2 (right from 1 then left from 4).
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return [-1, -1, -1]
            left, right = dfs(root.left), dfs(root.right)
            return [
                left[1] + 1,
                right[0] + 1,
                max(left[1] + 1, right[0] + 1, left[2], right[2]),
            ]

        return dfs(root)[-1]


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(8)
    print(sol.longestZigZag(root))
