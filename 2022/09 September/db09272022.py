"""
This question is asked by Amazon.
Given the root of a binary tree where every node’s value is either 0 or 1
remove every subtree that does not have a 1 in it.

Ex: Given the following binary tree…

        1
      /   \
    1      0
Return the tree such that it’s been modified to look as follows…
        1
      /
    1
Ex: Given the following binary tree…

        1
      /   \
    1      1
Return the tree such that it’s been modified to look as follows…
        1
      /   \
    1      1
(No modifications are necessary)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pruneTree(self, root):
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return None if root.val == 0 and not root.left and not root.right else root


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.pruneTree([1, 1, 0, 1, 1, 0, 1, 0]))
