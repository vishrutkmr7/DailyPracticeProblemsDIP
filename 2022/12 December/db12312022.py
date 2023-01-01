"""Given the reference to the root of a binary tree, return a list containing all the “only children”’s values. An “only child” is a node that is the sole node under its parent node. 
Note: The root node is not be considered an only child. 

Ex: Given the following root…

        1
      /   \
     2     4
       \
        7, return [7].
Ex: Given the following root…

        1
      /   \
     2     3 return [].
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def onlyChild(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        if root.left is None:
            if root.right is None:
                return []
            return [root.right.val] + self.onlyChild(root.right)
        if root.right is None:
            return [root.left.val] + self.onlyChild(root.left)
        return self.onlyChild(root.left) + self.onlyChild(root.right)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.onlyChild(TreeNode(1, TreeNode(2, None, TreeNode(7)), TreeNode(4))))
    print(solution.onlyChild(TreeNode(1, TreeNode(2), TreeNode(3))))
