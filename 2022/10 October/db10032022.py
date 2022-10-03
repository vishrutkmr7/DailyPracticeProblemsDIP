"""
Given the reference to a binary search tree, return the kth smallest value in the tree.

Ex: Given the following binary search tree and value k…

    3
   / \
  2   4, k = 1, return 2.
Ex: Given the following binary search tree and value k…

    7
   / \
  3   9
   \
    5, k = 3, return 7.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.kthSmallest(TreeNode(3, TreeNode(2), TreeNode(4)), 1) == 2
    assert (
        solution.kthSmallest(
            TreeNode(7, TreeNode(3, None, TreeNode(5)), TreeNode(9)), 3
        )
        == 7
    )
    print("All tests passed.")
