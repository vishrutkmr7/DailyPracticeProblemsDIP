"""Given the root of a binary tree that contains only unique values, and two tree values x and y,
return whether or not the nodes containing values x and y are cousins.
Note: Two nodes in a tree are cousins if they have the same depth but different parents.

Ex: Given the following root, x, and y…

      1
    /   \
   2     3, x = 2, y = 3, return false (2 and 3 are on the same level but have the same parent).
Ex: Given the following root, x, and y…

      5
    /   \
   3     2
  / \   / \
 4  7  9   8, x = 8, y = 4, return true.
"""


class TreeNode:
    """Binary tree node"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """Returns whether or not the nodes containing values x and y are cousins"""
        levelFound = -1
        ans = False
        foundRoot = -1

        def helper(curr=root, level=0, par=0):
            nonlocal levelFound, ans, foundRoot
            if curr:
                if curr.val in [x, y]:
                    if levelFound + 1 and foundRoot + 1:
                        ans = levelFound == level and foundRoot != par
                        return
                    else:
                        levelFound = level
                        foundRoot = par
                helper(curr.left, level + 1, curr.val)
                helper(curr.right, level + 1, curr.val)
            return

        helper()
        return ans


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(8)
    print(solution.isCousins(root, 8, 4))

    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.isCousins(root, 2, 3))
