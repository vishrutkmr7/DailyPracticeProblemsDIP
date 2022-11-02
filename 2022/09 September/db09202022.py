"""
Given a binary tree, return the bottom-left most value.
Note: You may assume each value in the tree is unique.
Ex: Given the following binary tree…

      1
     / \
    2   3
   /
  4 
return 4.
Ex: Given the following binary tree…

      8
     / \
    1   4
       /
      2 
return 2.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    # Example 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(solution.findBottomLeftValue(root))

    # Example 2
    root = TreeNode(8)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    print(solution.findBottomLeftValue(root))
