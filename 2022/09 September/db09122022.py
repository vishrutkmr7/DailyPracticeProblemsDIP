"""
This question is asked by Amazon.
Given two trees s and t return whether or not t is a subtree of s.
Note: For t to be a subtree of s not only must each node’s value in t
match its corresponding node’s value in s, but t must also exhibit the exact same structure as s.
You may assume both trees s and t exist.

Ex: Given the following trees s and t…

s = 1
   / \
  3   8
t = 1
     \
      8
return false
Ex: Given the following trees s and t…

s = 7
   / \
  8   3
t = 7
   / \
  8   3
return true
Ex: Given the following trees s and t…

s = 7
   / \
  8   3
t = 7
   / \
  8   3
     /
    1
return false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    s = TreeNode(1, TreeNode(3), TreeNode(8))
    t = TreeNode(1, None, TreeNode(8))
    assert solution.isSubtree(s, t) is False
    print(solution.isSubtree(s, t))
    s = TreeNode(7, TreeNode(8), TreeNode(3))
    t = TreeNode(7, TreeNode(8), TreeNode(3))
    assert solution.isSubtree(s, t) is True
    print(solution.isSubtree(s, t))
    s = TreeNode(7, TreeNode(8), TreeNode(3))
    t = TreeNode(7, TreeNode(8), TreeNode(3, TreeNode(1)))
    assert solution.isSubtree(s, t) is False
    print(solution.isSubtree(s, t))
