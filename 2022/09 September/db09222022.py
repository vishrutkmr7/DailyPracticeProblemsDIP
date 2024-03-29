"""
Given the reference to a binary search tree and a value to insert,
return a reference to the root of the tree after the value has been inserted in a position
that adheres to the invariants of a binary search tree.
Note: It is guaranteed that each value in the tree, including the value to be inserted, is unique.

Ex: Given the following tree and value…

      2
     / \
    1   3
value = 4, return the following tree...
      2
     / \
    1   3
         \
          4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def traverse(self):
        print(self.val)
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.traverse()
    print("After Insertion")
    root = solution.insertIntoBST(root, 4)
    root.traverse()
