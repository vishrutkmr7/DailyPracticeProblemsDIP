"""
Given the root of a binary tree, return the total number of subtrees that all contain
the same value.

Ex: Given the following binary tree...

          2
        /   \
       5     7
     /   \     \
    3     3     7, return 4 (both threes and both sevens).
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0

        def helper(root):
            if not root:
                return True
            left = helper(root.left)
            right = helper(root.right)
            if left and right:
                if root.left and root.left.val != root.val:
                    return False
                if root.right and root.right.val != root.val:
                    return False
                self.count += 1
                return True
            return False

        helper(root)

        return self.count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(5)
    root.right = TreeNode(7)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(7)
    print(solution.countUnivalSubtrees(root))
