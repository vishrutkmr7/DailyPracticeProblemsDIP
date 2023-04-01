"""
Given the reference to the root of a binary tree, return the sum of all leaves at the deepest level.

Ex: Given the following tree…

      2
     / \
    4   5, return 9 (4 and 5 are at the deepest level and sum to 9).
Ex: Given the following tree…

      1
       \
        2
         \
          3, return 3.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level_sum


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.deepestLeavesSum(TreeNode(2, TreeNode(4), TreeNode(5))))
    print(solution.deepestLeavesSum(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))))
