"""
You’re a thief trying to rob a binary tree. As a thief, you are trying to steal as much
money as possible. The amount of money you steal is equivalent to the sum of all the node’s
values that you decide to rob. If two adjacent nodes are robbed, the authorities are
automatically alerted. Return the maximum loot that you can steal without alerting the authorities.

Ex: Given the following binary tree...

        2
      /   \
     5     7, return 12 (5 + 7 = 12).
Ex: Given the following binary tree...

        4
      /   \
     3     2
      \     \
       9     7, return 20 (4 + 9 + 7 = 20).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root):
        def helper(root):
            if not root:
                return 0, 0
            left = helper(root.left)
            right = helper(root.right)
            return max(left) + max(right), root.val + left[0] + right[0]

        return max(helper(root))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.rob(TreeNode(2, TreeNode(5), TreeNode(7))))
    print(
        solution.rob(
            TreeNode(4, TreeNode(3, right=TreeNode(9)), TreeNode(2, right=TreeNode(7)))
        )
    )
