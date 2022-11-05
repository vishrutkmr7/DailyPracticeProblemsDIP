"""Given the reference to a binary search tree, “level-up” the tree.
Leveling-up the tree consists of modifying every node in the tree such that every node’s
value increases by the sum of all the node’s values that are larger than it.
Note: The tree will only contain unique values and you may assume that it is a
valid binary search tree.

Ex: Given a reference to the following binary search tree...

      0
       \
        3, modify the tree such that it becomes...
      3
       \
        3
Ex: Given a reference to the following binary search tree...

      2
    /   \
   1     3, modify the tree such that it becomes...
      5
    /   \
   6     3"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelUp(self, root):
        def helper(root, total):
            if not root:
                return total
            root.val += helper(root.right, total)
            return helper(root.left, root.val)

        helper(root, 0)
        return root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.levelUp(TreeNode(0, right=TreeNode(3))))
    print(solution.levelUp(TreeNode(2, TreeNode(1), TreeNode(3))))
