"""
This question is asked by Facebook.
Given a reference to the root of a binary tree, return a list containing the average value in each level of the tree.

Ex: Given the following binary tree…

       1
      / \
    6    8
   / \ 
  1   5 
return [1.0, 7.0, 3.0]
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = [(root, 0)]
        result = []
        total_level = 0
        if not root:
            return []
        while queue:
            node, level = queue.pop(0)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            if result and total_level < level or not result:
                result.append([node.val])
            else:
                result[-1].append(node.val)
            total_level = max(level, total_level)
        return result

    def Average(self, lst):
        return sum(lst) / len(lst)

    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        return [self.Average(level) for level in self.levelOrder(root)]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1, TreeNode(6, TreeNode(1), TreeNode(5)), TreeNode(8))
    print(solution.averageOfLevels(root))
