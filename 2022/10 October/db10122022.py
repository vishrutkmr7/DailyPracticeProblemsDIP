"""
Given the reference to a binary tree, return the length of the longest path
in the tree that contains consecutive values.
Note: The path must move downward in the tree.
Ex: Given the following binary tree…

1
 \
  2
   \
    3
return 3.
Ex: Given the following binary tree…

       1
      / \
     2   2
    / \ / \
   4  3 5  8
     /
    4
return 4.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root):
        self.longest = 0
        self.dfs(root, None, 0)
        return self.longest

    def dfs(self, node, parent, length):
        if not node:
            return
        length = length + 1 if parent and node.value == parent.value + 1 else 1
        self.longest = max(self.longest, length)
        self.dfs(node.left, node, length)
        self.dfs(node.right, node, length)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(solution.longestConsecutive(root))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(4)
    print(solution.longestConsecutive(root))
