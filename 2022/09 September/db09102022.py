"""
This question is asked by Facebook.
Given the root of a binary tree and two values low and high return the sum
of all values in the tree that are within low and high.

Ex: Given the following tree where low = 3 and high = 5…

        1
       / \
      7   5
    /    / \
   4    3   9
return 12 (3, 4, and 5 are the only values within low and high and they sum to 12)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def BST_array(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        return self.BST_array(root.left) + [root.val] + self.BST_array(root.right)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        values = self.BST_array(root)
        return sum(val for val in values if low <= val <= high)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.rangeSumBST(
            TreeNode(
                1, TreeNode(7, TreeNode(4)), TreeNode(5, TreeNode(3), TreeNode(9))
            ),
            3,
            5,
        )
    )
